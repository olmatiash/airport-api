from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from flights.models import (
    Flight,
    Airport,
    Route,
    Order,
    Ticket,
    AirplaneType,
    Airplane,
    Crew
)
from flights.serializers import (
    FlightSerializer,
    AirportSerializer,
    RouteSerializer,
    OrderSerializer,
    TicketSerializer,
    AirplaneTypeSerializer,
    AirplaneSerializer,
    CrewSerializer
)


class FlightViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [AllowAny]


class AirportViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [AllowAny]


class RouteViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [AllowAny]


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.prefetch_related("tickets")
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class TicketViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Ticket.objects.select_related("order", "flight")
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)


class AirplaneTypeViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer
    permission_classes = [AllowAny]


class AirplaneViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = [AllowAny]


class CrewViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [IsAuthenticated]
