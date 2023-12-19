from django.urls import path, include
from rest_framework import routers

from flights.views import (
    OrderViewSet,
    FlightViewSet,
    AirportViewSet,
    RouteViewSet,
    TicketViewSet,
    AirplaneTypeViewSet,
    AirplaneViewSet,
    CrewViewSet,
)

router = routers.DefaultRouter()
router.register("flights", FlightViewSet)
router.register("airports", AirportViewSet)
router.register("routes", RouteViewSet)
router.register("orders", OrderViewSet)
router.register("tickets", TicketViewSet)
router.register("airplane_types", AirplaneTypeViewSet)
router.register("airplanes", AirplaneViewSet)
router.register("crews", CrewViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "flights"
