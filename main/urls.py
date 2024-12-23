from django.urls import path
from main.views import first_page, create_item_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, login_user, logout_user, register, edit_item, delete_item, add_item_entry_ajax, create_item_entry_flutter

app_name = 'main'

urlpatterns = [
    path('', first_page, name='first_page'),
    path('simple_item_form/', create_item_entry, name='create_item_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('edit/<uuid:id>', edit_item, name='edit_item'),
    path('delete/<uuid:id>', delete_item, name='delete_item'),
    path('create-item-entry-ajax', add_item_entry_ajax, name='add_item_entry_ajax'),
    path('create-item-flutter/', create_item_entry_flutter, name='create_item_entry_flutter'),
]