from django.shortcuts import render,redirect
from vage.models import *
from django.http import HttpResponse
from django.http import request
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def receipes(request):
    if request.method =="POST":
         
         data = request.POST
         receipe_image = request.FILES.get('receipe_image')
         receipe_name = data.get('receipe_name')
         receipe_description = data.get('receipe_description')
         
#create a add data

         Receipe.objects.create(
               receipe_image=  receipe_image,
               receipe_name= receipe_name,
               receipe_description= receipe_description,
               )
         return redirect('/receipes/')
    
    queryset = Receipe.objects.all()

    #Seach element
    
    if request.GET.get('search'):
         queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))
         
    
    context = {'receipes': queryset}
    return render(request, 'receipes.html',context)

#Create a updata frunction


def update_receipe(request, id):
      queryset = Receipe.objects.get(id = id)

      if request.method == "POST":
           data = request.POST

           receipe_image = request.FILES.get('receipe_image')
           receipe_name = data.get('receipe_name')
           receipe_description = data.get('receipe_description') 

           queryset.receipe_name = receipe_name
           queryset.receipe_description = receipe_description

           if receipe_image:
                queryset.receipe_image = receipe_image

      queryset.save()




      context = {'receipe': queryset}
     

      return render(request, 'update_receipes.html',context)

     

#Create a delete function 

def delete_receipe(request, id):
     queryset = Receipe.objects.get(id = id)
     queryset.delete()
     return redirect('/receipes/')


#Login form

def login_page(request):

      if request.method == "POST":
          username = request.POST.get('username')
          password = request.POST.get('password')

          if not User.objects.filter(username = username).exists():
                messages.info(request, 'Invaild Username')
                return redirect('/login/')
          
          user = authenticate(username = username , password = password)
          
          if user is None:
               messages.info(request, 'Invaild Password')
               return redirect('/login/')
          
          else:
               login(request ,user)
               return redirect('/receipes/')

      return render(request , 'login.html')
#logout page

def logout_page(request):
     logout(request)
     return redirect('/login/')

#register form
def register(request):

     if request.method == "POST":
          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
          username = request.POST.get('username')
          password = request.POST.get('password')

          user = User.objects.filter(username = username)

          if user.exists():
               messages.info(request, 'User alread taken')
               return redirect('/register/')



          user = User.objects.create(
               first_name = first_name,
               last_name = last_name,
               username = username,
               )
          
          user.set_password(password)
          user.save()

          messages.info(request, 'Account created Successfully')

          return redirect('/register/')
     
     return render(request , 'register.html')




    
          
          
               


     


     