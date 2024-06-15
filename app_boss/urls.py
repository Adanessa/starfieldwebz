from django.urls import path
from . import views

urlpatterns = [
    path('weapons/search/', views.weapon_search, name='weapon_search'),
]
