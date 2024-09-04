from django.urls import path
from main.views import first_page
app_name = 'main'

urlpatterns = [
    path('', first_page, name='first_page'),
]