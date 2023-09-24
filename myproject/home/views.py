from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {'page' : 'home'}
    peoples = [
        {'name' : 'meet pansuriya', 'age' :21},
        {'name' : 'bansil nariya', 'age' :10},
        {'name' : 'pratic chikhaliya', 'age' :22},
        {'name' : 'jay patel', 'age' :17},
        {'name' : 'parth pansuriya', 'age' :20},
    ]

    for people in peoples:
        if people['age']:
            print("yes")     
    
    vegerables = ['Pumkin','Tomato','potato']

    return render(request, "index.html", context={'peoples':peoples ,'vegerables':vegerables})
    

def sucess_page(request):
    context = {'page' : 'sucess_page'}
    print("*" * 10)
    return HttpResponse("<h1>hello i am meet, i am fin</h1>",context)

def about(request):
    context = {'page' : 'about'}
    return render(request, "about.html",context)

def contact(request):
    context = {'page' : 'contact'}
    return render(request, "contact.html",context)