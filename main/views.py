from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import ItemEntryForm
from main.models import Item

# Create your views here.

def first_page(request):
    item_entries = Item.objects.all()
    context = {'application':'Simple PBP E-Shop','app':'main','name':'Vander Gerald Sukandi','NPM':'1906350603','class':'PBP A', 'it_entries' : item_entries}
    return render(request,'first_page.html', context)

def create_item_entry(request):
    form = ItemEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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


