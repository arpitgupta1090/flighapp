from flightapp.models import Flight, Passenger, Reservation
from flightapp.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsAuthenticated,)


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class FlightSearch(APIView):

    def get(self, request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

    def post(self, request):
        flights = Flight.objects.filter(departureCity=request.data['departureCity'],
                                        arrivalCity=request.data['arrivalCity'],
                                        dateOfDeparture=request.data['dateOfDeparture'])
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)
