from django.contrib import admin
from .models import Shipment, Agent, Client, Shipment_Category, Shipment_Tags, Shipmemt_history, Package
# Register your models here.


admin.site.register(Shipment)
admin.site.register(Agent)
admin.site.register(Client)
admin.site.register(Shipment_Category)
admin.site.register(Shipment_Tags)
admin.site.register(Shipmemt_history)
admin.site.register(Package)