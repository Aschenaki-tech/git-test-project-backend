from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet, UserRegistrationView, CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='song')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/register/', UserRegistrationView.as_view(), name='user-register'),
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
