from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', home, name='home'),  # Add this line
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),  # Route for authentication
    path('students/', include('students.urls')),  # Route for students app
]
