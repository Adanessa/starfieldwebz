from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.weapon_search, name='weapon_search'),
    path('all/', views.display_all_items, name='display_all_items'),
]
