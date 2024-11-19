from .views import (
dashboard,
add_category,
add_tags, 
add_clients,
agent,
add_shipment,
shipment_list,
shipment_update_view,
tracking,
delete_shipment
) 
from django.urls import path


urlpatterns = [
		path('', dashboard, name="dashboard"),
		path('add-category/', add_category, name="add-category"),
		path('add-tags/', add_tags, name="add_tags"),
		path('add-clients/', add_clients, name="add_clients"),
		path('add-agent/', agent, name="add_agent"),
		path('add-shipment/', add_shipment, name="add_shipment"),
		path('shipment-list/', shipment_list, name="shipment_list"),
		path('shipment_update_view/<int:id>/', shipment_update_view, name='shipment_update_view'),
		path('shipment_delete/<int:shipment_id>/', delete_shipment, name='delete_shipment'),
		path('track-status', tracking, name='tracking'),
	]