from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weapons/', include('weapons.urls')),
    path('armor/', include('armor.urls')),
]
