# Generated by Django 4.2.4 on 2023-08-18 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Receipe_name', models.CharField(max_length=100)),
                ('Receipe_description', models.TextField()),
                ('Receipe_image', models.ImageField(upload_to='receipe')),
            ],
        ),
    ]
