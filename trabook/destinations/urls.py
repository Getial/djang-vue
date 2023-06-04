from django.urls import path
from .views import DestinationViewSet, VacationPlanViewSet, BlogViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('destinations', DestinationViewSet, basename='destination')
router.register('vacationplans', VacationPlanViewSet, basename='vacationplans')
router.register('blogs', BlogViewSet, basename="blogs")

urlpatterns = router.urls