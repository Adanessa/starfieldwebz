from django.urls import path
from . import views

app_name = 'weapons'

urlpatterns = [
    path('', views.weapon_gallery, name='weapon_gallery'),
    path('<int:weapon_id>/', views.weapon_detail, name='weapon_detail'),
]
