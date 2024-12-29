from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),  # Ensure this line includes your auth app URLs
    path('api/', include('api.urls')),              # Ensure this line includes your API app URLs
]
