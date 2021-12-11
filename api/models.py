from django.db import models


class Weather(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temparature = models.DecimalField(max_digits=12, decimal_places=2)
    humidity = models.IntegerField()
    wind_speed = models.DecimalField(max_digits=12, decimal_places=2)
    clouds = models.IntegerField()
    description = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    def __str__(self):
        return f"Weather data {self.city}: {self.timestamp}"
