from django.urls import path
from . import views

app_name = 'armor'

urlpatterns = [
    path('display/', views.display_all_armor_stuff, name='display_all_armor_stuff'),
]