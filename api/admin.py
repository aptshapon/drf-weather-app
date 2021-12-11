from django.contrib import admin
from api.models import Weather


@admin.register(Weather)
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "city",
        "timestamp",
        "temparature",
        "humidity",
        "wind_speed",
        "description",
        "clouds",
    )
    list_filter = ("id", "city")
