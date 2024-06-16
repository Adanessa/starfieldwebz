from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('search/', views.search_form, name='search_form'),
    path('search/results/', views.search_items, name='search_results'),
]
