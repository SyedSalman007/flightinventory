from rest_framework.routers import DefaultRouter

from flightinventory.users.api.views import UserViewSet

router = DefaultRouter()

router.register("users", UserViewSet)

app_name = "users"
urlpatterns = router.urls
