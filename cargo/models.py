from django.db import models

# Create your models here.

class Cargo(models.Model):
	shipment_logo = models.ImageField(upload_to="logo")
	email = models.EmailField()
	email_subject = models.CharField(max_length=100,null=True, blank=True )

	def __str__(self):
		return self.email


class ShipmentMethod(models.Model):
	type_of_shipment = models.CharField(max_length=100, blank=True, unique=True)

	def __str__(self):
		return self.type_of_shipment



class ShipmentMode(models.Model):
	shipment_mode = models.CharField(max_length=100, blank=True, unique=True)

	def __str__(self):
		return self.shipment_mode


class ShipmentLocation(models.Model):
	shipment_location = models.CharField(max_length=100, blank=True, unique=True)

	def __str__(self):
		return self.shipment_location



class ShipmentCarrier(models.Model):
	shipment_carrier = models.CharField(max_length=100, blank=True, unique=True)

	def __str__(self):
		return self.shipment_carrier


class PaymentMethod(models.Model):
	payment_mode = models.CharField(max_length=100, blank=True, unique=True)

	def __str__(self):
		return self.payment_mode


class ShipmentStatus(models.Model):
	shipment_status = models.CharField(max_length=100, blank=True, unique=True)

	def __str__(self):
		return self.shipment_status



class PieaceType(models.Model):
	pieace_type = models.CharField(max_length=100, blank=True, unique=True)

	def __str__(self):
		return self.pieace_type
