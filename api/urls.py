from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.views import WeatherViewSet

router = DefaultRouter()
router.register("api", WeatherViewSet, basename="weather-data")

urlpatterns = [
    path("", include(router.urls)),
]
