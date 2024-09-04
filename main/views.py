from django.shortcuts import render, redirect

# Create your views here.

def first_page(request):
    context = {'application':'Simple PBP E-Shop','app':'main','name':'Vander Gerald Sukandi','NPM':'1906350603','class':'PBP A'}
    return render(request,'first_page.html', context)
