from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

from users.views import profile_views
from users.views.micro_auth import GetUserIdView

router = DefaultRouter()

router.register('admin/users', profile_views.AdminUserViewSet, basename='admin_user')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get_user_id/', GetUserIdView.as_view())
] + router.urls
