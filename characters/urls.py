from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('sarah_morgan/', views.sarah_morgan_detail, name='sarah_morgan_detail'),
    path('andreja/', views.andreja_detail, name='andreja_detail'),
    path('amundsen_barret/', views.amundsen_barret, name='amundsen_barret'),
    path('sam_coe/', views.sam_coe, name='sam_coe'),
    path('heller/', views.heller, name='heller'),
]
