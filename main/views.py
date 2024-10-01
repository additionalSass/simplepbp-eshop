from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect
from django.urls import reverse
from main.forms import ItemEntryForm
from main.models import Item
import datetime

# Create your views here.

@login_required(login_url='/login')
def first_page(request):
    item_entries = Item.objects.all()
    context = {
        'application':'Simple PBP E-Shop',
        'app':'main',
        'name':'Vander Gerald Sukandi',
        'NPM':'1906350603',
        'class':'PBP A',
        'it_entries' : item_entries,
        'last_login' : request.COOKIES['last_login'],
        'current_username' : request.user.username,
    }
    return render(request,'first_page.html', context)

@login_required(login_url='/login')
def create_item_entry(request):
    form = ItemEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        it_entry = form.save(commit=False)
        it_entry.user = request.user
        it_entry.save()
        return redirect('main:first_page')

    context = {'form': form}
    return render(request, "create_item_entry.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form,}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:first_page"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def edit_item(request, id):
    item = Item.objects.get(pk = id)

    # Set item entry sebagai instance dari form
    form = ItemEntryForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:first_page'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

@login_required(login_url='/login')
def delete_item(request, id):
    # Get mood berdasarkan id
    item = Item.objects.get(pk = id)
    # Hapus mood
    item.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:first_page'))