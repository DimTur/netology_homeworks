from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=30, verbose_name='Датчик')
    description = models.CharField(max_length=300, verbose_name='Описание')

    class Meta:
        ordering = ['-id']


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата')

    class Meta:
        ordering = ['-created_at']