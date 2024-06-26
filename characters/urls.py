from django.urls import path
from . import views

app_name = 'characters'

urlpatterns = [
    path('<int:character_id>/', views.character_detail, name='character_detail'),
]
