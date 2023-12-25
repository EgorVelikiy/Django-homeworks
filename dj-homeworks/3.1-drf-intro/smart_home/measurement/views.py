from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorsSerializer, MeasurementSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer

    def post(self, request):
        Sensor(name=request.data["name"], description=request.data["description"]).save()
        return Response("ok")


class SensorChange(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        Sensor(id=pk, description=request.data["description"]).save()
        return Response("ok")


class MeasurementCreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request, pk):
        sensor_id = Sensor.objects.get(id=pk)
        Measurement(sensor_id=sensor_id, description=request.data["description"]).save()
        return Response("ok")