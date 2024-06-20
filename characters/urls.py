from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('sarah_morgan/', views.sarah_morgan_detail, name='sarah_morgan_detail'),
]
