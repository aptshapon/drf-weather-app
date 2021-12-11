from apscheduler.schedulers.background import BackgroundScheduler

from api.views import WeatherViewSet


def start():
    scheduler = BackgroundScheduler()
    weather = WeatherViewSet()
    scheduler.add_job(weather.save_weather_api, "interval", minutes=1)
    scheduler.start()
