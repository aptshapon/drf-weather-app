from rest_framework import viewsets
import requests
from api.models import Weather
from api.serializer import WeatherSerializer


class WeatherViewSet(viewsets.ModelViewSet):

    serializer_class = WeatherSerializer

    def get_queryset(self):
        return Weather.objects.all()

    def _weather_api(self):
        url = "http://api.openweathermap.org/data/2.5/weather?q=Dhaka,bd&APPID=04d721e6c81b10cfd0a3da439e554692"
        api_request = requests.get(url)

        try:
            api_request.raise_for_status()
            return api_request.json()
        except:
            return None

    def save_weather_api(self):
        request_data = self._weather_api()
        print(request_data)
        if request_data is not None:
            try:
                Weather.objects.create(
                    temparature=request_data["main"]["temp"],
                    humidity=request_data["main"]["humidity"],
                    wind_speed=request_data["wind"]["speed"],
                    description=request_data["weather"][0]["description"],
                    clouds=request_data["clouds"]["all"],
                    city=request_data["name"],
                )
                request_data.save()
            except:
                pass
