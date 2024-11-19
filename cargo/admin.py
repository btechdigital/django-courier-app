from django.contrib import admin
from .models import Cargo, ShipmentMethod, ShipmentMode, ShipmentLocation, ShipmentCarrier, PaymentMethod, ShipmentStatus, PieaceType
# Register your models here.

admin.site.register(Cargo)
admin.site.register(ShipmentMethod)
admin.site.register(ShipmentMode)
admin.site.register(ShipmentLocation)
admin.site.register(ShipmentCarrier)
admin.site.register(PaymentMethod)
admin.site.register(ShipmentStatus)
admin.site.register(PieaceType)
