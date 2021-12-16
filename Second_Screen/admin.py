from django.contrib import admin
from .models import Users
from .models import ParkingList


admin.site.register(Users)
admin.site.register(ParkingList)