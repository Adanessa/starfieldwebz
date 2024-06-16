from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('search/', views.item_search, name='item_search'),
]
