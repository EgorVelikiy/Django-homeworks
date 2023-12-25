from django.urls import path

from measurement.views import SensorsView, SensorChange, MeasurementCreate

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensor/<pk>/', SensorChange.as_view()),
    path('measurement/', MeasurementCreate.as_view())
]
