from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'main_site'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('planets/', include('planets.urls')),
    path('weapons', include('weapons.urls')),
    path('', views.index, name='index'),
]
