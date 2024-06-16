from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('search/', views.search_items, name='search_items'),
    path('search/results/' view.search_items, name='search_results'),
]
