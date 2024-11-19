from django.db import models
from cargo.models import Cargo, ShipmentMethod, ShipmentMode, ShipmentLocation, ShipmentCarrier, ShipmentStatus, PaymentMethod, PieaceType
# Create your models here.

class Shipment_Tags(models.Model):
	name = models.CharField(max_length=20, unique=True)
	description = models.TextField(null=True, blank=True,)

	def __str__(self):
		return self.name


class Shipment_Category(models.Model):
	name = models.CharField(max_length=20, unique=True)
	description = models.TextField(null=True, blank=True,)

	def __str__(self):
		return self.name


class Client(models.Model):
	First_Name = models.CharField(max_length=20,null=True, blank=True,)
	Last_Name = models.CharField(max_length=20,null=True, blank=True,)
	website = models.CharField(max_length=10,null=True, blank=True,)
	email = models.EmailField()

	def __str__(self): 
		return self.First_Name


class Agent(models.Model):
	First_Name = models.CharField(max_length=20,null=True, blank=True,)
	Last_Name = models.CharField(max_length=20,null=True, blank=True,)
	website = models.CharField(max_length=10,null=True, blank=True,)
	email = models.EmailField()

	def __str__(self):
		return self.First_Name





class Shipment(models.Model):
    Is_publish = (
        ("yes", "yes"),
        ("no", "no")
    )
    tracking_no = models.CharField(max_length=20, null=False, blank=False)
    shipper_name = models.CharField(max_length=100, null=False, blank=False)
    shipper_phone = models.CharField(max_length=50, null=False, blank=False)
    shipper_address = models.CharField(max_length=200, null=False, blank=False)
    shipper_email = models.EmailField(null=False, blank=False)

    receivers_name = models.CharField(max_length=100, null=False, blank=False)
    receivers_phone = models.CharField(max_length=50, null=False, blank=False)
    receivers_address = models.CharField(max_length=200, null=False, blank=False)
    receivers_email = models.EmailField(null=False, blank=False)

    shipment_method = models.ForeignKey(ShipmentMethod, on_delete=models.DO_NOTHING, null=False)
    weight = models.CharField(max_length=50, null=False, blank=False)
    package = models.CharField(max_length=150, null=False, blank=False)
    product = models.CharField(max_length=200, null=False, blank=False)
    payment_mode = models.ForeignKey(PaymentMethod, on_delete=models.DO_NOTHING, null=True, related_name='payment_mothod')
    carrier = models.ForeignKey(ShipmentCarrier, on_delete=models.DO_NOTHING, null=False, related_name='carrier')
    departure_time = models.TimeField()
    destination = models.ForeignKey(ShipmentLocation, on_delete=models.DO_NOTHING, null=False, related_name='destination')
    pickup_time = models.TimeField()
    comment = models.TextField(null=True, blank=True)

    courier_name = models.CharField(max_length=100, null=False, blank=False)
    mode = models.ForeignKey(ShipmentMode, on_delete=models.DO_NOTHING, null=False, related_name='mode')
    quantity = models.CharField(max_length=50, null=False, blank=False)
    total_frieght = models.FloatField(null=False, blank=False)
    carrier_reference_no = models.CharField(max_length=50, null=True, blank=True)
    origin = models.ForeignKey(ShipmentLocation, on_delete=models.DO_NOTHING, null=False, related_name='origin')
    pickup_date = models.DateField(auto_now_add=False, null=False, blank=False)
    expected_delivery_date = models.DateField(auto_now_add=False, null=False, blank=False)

    feature_image = models.ImageField(upload_to='shipment-images', null=True, blank=True)
    category = models.ForeignKey(Shipment_Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ForeignKey(Shipment_Tags, on_delete=models.CASCADE, null=True, blank=True)
    shipment_client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    shipment_agent = models.ForeignKey(Agent, on_delete=models.CASCADE,null=True, blank=True)
    publish = models.CharField(choices=Is_publish, max_length=3, default="no")

    def __str__(self):
        return self.tracking_no

    def get_status(self):
        return self.shipment_history_set.all()


class Shipmemt_history(models.Model):
    Is_Status = (
        ("Pending", "Pending"),
        ("Picked up", "Picked up"),
        ("Picked up", "Picked up"),
        ("On Hold", "On Hold"),
        ("Out for delivery", "Out for delivery"),
        ("In Transit", "In Transit"),
        ("Enroute", "Enroute"),
        ("Cancelled", "Cancelled"),
        ("Delivered", "Delivered"),
        ("Returned", "Returned"),


    )
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=False, blank=False, related_name="shipment_history")
    lacation = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(choices=Is_Status, max_length=100, null=True, blank=True, default="Pending")
    remark = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=False, null=False, blank=False)
    time = models.TimeField()
    updated_by = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.shipment.tracking_no





class Package(models.Model):
    Piece_type = (
        ("Pallet", "Pallet"),
        ("Carton", "Carton"),
        ("Loose", "Loose"),
        ("Crate", "Crate"),
        ("Others", "Others"),

    )
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, null=False, blank=False, related_name="shipment_package")
    quantity = models.FloatField(null=False, blank=False)
    Piece_type = models.CharField(choices=Piece_type, max_length=100, null=True, blank=True, default="Pending")
    description = models.TextField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=False, blank=False)
    height = models.FloatField(null=True, blank=True)
    value = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.shipment.tracking_no



