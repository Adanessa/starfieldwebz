from django.urls import path
from . import views

app_name = 'planets'

urlpatterns = [
    path('results/', views.search_results, name='search_results'),
]