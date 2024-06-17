from django.contrib import admin
from django.urls import path, include
from main_site import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name="index"),
    path('weapons/', include('weapons.urls')),
    path('armor/', include('armor.urls')),
    path('items/', include('items.urls')),
    path('planets/', include('planets.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('', include('main_site.urls')),
]
