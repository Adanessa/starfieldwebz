from django.urls import path
from . import views

app_name = 'planets'

urlpatterns = [
    path('search/', views.resource_search, name='resource_search')
]
