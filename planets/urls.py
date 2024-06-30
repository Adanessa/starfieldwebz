from django.urls import path
from . import views

app_name = 'planets'

urlpatterns = [
    path('search/', views.search_planets, name='search_planets'),
    path('planet_table/', views.planet_table, name='planet_table'),

]
