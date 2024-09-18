from django.forms import ModelForm
from main.models import Item

class ItemEntryForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "description","stocks"]