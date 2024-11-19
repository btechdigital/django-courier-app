from django.urls import path
from .views import (
	settings,
	add_shipment_method, 
	add_shipment_mode, 
	add_shipment_location, 
	add_shipment_carrier, 
	add_payment_method,
	add_shipment_status,
	update_shipment_status,
	delete_status,
	update_payment_method,
	delete_payment,
	update_shipment_carrier,
	delete_carrier,
	update_shipment_location,
	update_shipment_mode,
	delete_mode,
	login,
	)



urlpatterns = [
		path('', login, name='login'),
		path('<id>', settings, name="setting"),
		path('add-shipment-method/', add_shipment_method, name="add_shipment_method"),
		path('add-shipment-mode/', add_shipment_mode, name="add_shipment_mode"),
		path('add-shipment-location/', add_shipment_location, name="add_shipment_location"),
		path('add-shipment-carrier/', add_shipment_carrier, name="add_shipment_carrier"),
		path('add-payment-method/', add_payment_method, name="add_payment_method"),
		path('add-shipment-status/', add_shipment_status, name="add_shipment_status"),


		path('update-shipment-status/<id>/', update_shipment_status, name="update_shipment_status"),
		path('delete-shipment-status/<id>/', delete_status, name="delete_status"),

		path('delete_payment_method/<id>/', delete_payment, name="delete_payment"),
		path('update_payment_method/<id>/', update_payment_method, name="update_payment_method"),

		path('update_carrier/<id>/', update_shipment_carrier, name="update_carrier"),
		path('delete_carrier/<id>/', delete_carrier, name="delete_carrier"),

		path('update_location/<id>/', update_shipment_location, name="update_location"),
		#path('delete_location/<id>/', delete_location, name="delete_location"),


		path('update_shipment_mode/<id>/', update_shipment_mode, name="update_mode"),
		path('delete_mode/<id>/', delete_mode, name="delete_mode"),

	]