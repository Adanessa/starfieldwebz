from django.urls import path
from . import views

urlpatterns = [
    path('display/', views.display_all_armor_stuff, name='display_all_armor_stuff'),
]