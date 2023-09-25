from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from uavrental.users.api.views import UserViewSet
from api.views import UavListViewSet  # Import your ViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("uavlists", UavListViewSet)  # Add this line to register the "uavlists" resource


app_name = "api"
urlpatterns = router.urls
