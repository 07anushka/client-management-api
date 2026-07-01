from rest_framework.routers import DefaultRouter

from .views import ClientPackageViewSet

router = DefaultRouter()

router.register(
    "",
    ClientPackageViewSet,
    basename="subscriptions",
)

urlpatterns = router.urls