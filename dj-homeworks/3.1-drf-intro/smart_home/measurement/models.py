from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement', verbose_name='ID датчика')
    temperature = models.FloatField(verbose_name='Температура')
    date = models.DateTimeField(auto_now_add=True)

