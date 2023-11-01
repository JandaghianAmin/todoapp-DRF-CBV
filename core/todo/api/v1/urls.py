# pylint: disable=import-error
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet


router = DefaultRouter()
router.register(r'tasks', TodoViewSet, basename="tasks")

urlpatterns = router.urls
