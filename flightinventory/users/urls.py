from rest_framework.routers import DefaultRouter
from django.urls import path
from flightinventory.users.api.views import UserLoginAPI, RefreshTokenGetter, UserSignupAPI
from flightinventory.users.api.views import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()

router.register("users", UserViewSet)

app_name = "users"

urlpatterns = [
    path("users/login/", UserLoginAPI.as_view(), name="login"),
    path("users/token/", RefreshTokenGetter.as_view(), name="token"),
    path("users/signup/", UserSignupAPI.as_view(), name="signup"),
    ]
urlpatterns += router.urls


# urlpatterns = [
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
# ]
