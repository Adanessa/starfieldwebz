from django.urls import path
from . import views

app_name = 'planets'

urlpatterns = [
    path('search/', views.search_planets, name='search_planets'),
    path('results/', views.search_results, name='search_results'),
]