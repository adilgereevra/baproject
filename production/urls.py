from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls')),
    path("catalog/", include("catalogapp.urls")), #catalog / catalogapp
]