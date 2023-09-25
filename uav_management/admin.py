from django.contrib import admin
from .models import UAV, UAVRental
# Register your models here.


admin.site.register(UAV),
admin.site.register(UAVRental)