from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import (
CargoForm,
ShipmentMethodForm,
ShipmentModeForm, 
ShipmentLocationForm,
ShipmentCarrierForm,
PaymentMethodForm,
ShipmentStatusForm,
UserForm
)

from .models import (
    ShipmentMethod,
    ShipmentMode,
    ShipmentLocation,
    ShipmentCarrier,
    PaymentMethod,
    ShipmentStatus,
    Cargo,
)

# Create your views here.




def login(request):
    if request.method == 'POST':
        form = UserForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login( request, user)
            messages.success(request, 'Login successful.')
            return redirect('dashboard')  # Replace 'dashboard' with the appropriate URL name
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
    else:
        form = UserForm()
    
    return render(request, 'dashboard/user/login.html', {'form': form})



def settings(request, id):
    cargo = get_object_or_404(Cargo, id=1)
    form = CargoForm( instance=cargo)
    if request.method == 'POST':
        form = CargoForm(request.POST, request.FILES, instance=cargo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Settings updated successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Error updating settings. Please check the form data.')
    else:
        form = CargoForm(instance=cargo)
    
    return render(request, 'dashboard/settings.html', {"form": form })


def add_shipment_method(request):
    shipment_method_list = ShipmentMethod.objects.all()
    if request.method == 'POST':
        form = ShipmentMethodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_shipment_method')
    else:
        form = ShipmentMethodForm()
    return render(request, 'dashboard/shipment_method.html', {"form": form, "shipment_method_list": shipment_method_list})



def add_shipment_mode(request):
    shipment_mode_list = ShipmentMode.objects.all()
    if request.method == 'POST':
        form = ShipmentModeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_shipment_mode')
    else:
        form = ShipmentModeForm()
    return render(request, 'dashboard/add_shipment_mode.html', {"form": form, "shipment_mode_list": shipment_mode_list})



def update_shipment_mode(request, id):
    shipment_mode = get_object_or_404(ShipmentMode, id=id)
    form = ShipmentModeForm(instance=shipment_mode)
    if request.method == 'POST':
        form = ShipmentModeForm(request.POST, instance=shipment_mode)
        if form.is_valid():
            form.save()
            return redirect('add_shipment_mode')
    return render(request, 'dashboard/update/mode.html', {"form": form})


def delete_mode(request, id):
    mode = get_object_or_404(ShipmentMode, id=id)
    mode.delete()
    return redirect('add_shipment_mode')




#----------------------------location ---------------------------------------

def add_shipment_location(request):
    shipment_location_list = ShipmentLocation.objects.all()
    if request.method == 'POST':
        form = ShipmentLocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_shipment_location')
    else:
        form = ShipmentLocationForm()
    return render(request, 'dashboard/add_shipment_location.html', {"form": form, "shipment_location_list": shipment_location_list})


def update_shipment_location(request, id):
    location = get_object_or_404(ShipmentLocation, id=id)
    form = ShipmentLocationForm( instance=location)
    if request.method == 'POST':
        form = ShipmentLocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('add_shipment_location')
    return render(request, 'dashboard/update/location.html', {"form": form})



# def delete_location(request, id):
#     location = get_object_or_404(ShipmentLocation, id=id)
#     location.delete()
#     return redirect('add_shipment_location')






#------------------------------- Shipment Carrier ------------------------------



def add_shipment_carrier(request):
    shipment_carrier_list = ShipmentCarrier.objects.all()
    if request.method == 'POST':
        form = ShipmentCarrierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_shipment_carrier')
    else:
        form = ShipmentCarrierForm()
    return render(request, 'dashboard/add_shipment_carrier.html', {"form": form, "shipment_carrier_list": shipment_carrier_list})


def update_shipment_carrier(request, id):
    carrier_method = get_object_or_404(ShipmentCarrier, id=id)
    form = ShipmentCarrierForm(instance=carrier_method)
    if request.method == 'POST':
        form = ShipmentCarrierForm(request.POST, instance=carrier_method )
        if form.is_valid():
            form.save()
            return redirect('add_shipment_carrier')
        
    return render(request, 'dashboard/update/carrier.html', {"form": form,})


def delete_carrier(request,id):
    carrier = get_object_or_404(ShipmentCarrier, id=id)
    carrier.delete()
    return redirect('add_shipment_carrier')


#-----------------------------------payment views --------------------------------



def add_payment_method(request):
    payment_method_list = PaymentMethod.objects.all()
    if request.method == 'POST':
        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_payment_method')
    else:
        form = PaymentMethodForm()
    return render(request, 'dashboard/add_payment_method.html', {"form": form, "payment_method_list": payment_method_list})


def update_payment_method(request, id):
    payment_method = get_object_or_404(PaymentMethod, id=id)
    form = PaymentMethodForm(instance=payment_method)
    if request.method == 'POST':
        form = PaymentMethodForm(request.POST, instance=payment_method )
        if form.is_valid():
            form.save()
            return redirect('add_payment_method')
        
    return render(request, 'dashboard/update/payment.html', {"form": form,})



def delete_payment(request, id):
    payment = get_object_or_404(PaymentMethod, id=id)
    payment.delete()
    return redirect('add_shipment_status')



# ------------------------------------status Views ------------------------------------------


def add_shipment_status(request):
    shipment_status_list = ShipmentStatus.objects.all()
    if request.method == 'POST':
        form = ShipmentStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_shipment_status')
    else:
        form = ShipmentStatusForm()
    return render(request, 'dashboard/add_shipment_status.html', {"form": form, "shipment_status_list": shipment_status_list})



def update_shipment_status(request, id):
    shipment_status = get_object_or_404(ShipmentStatus, id=id)
    form = ShipmentStatusForm(instance=shipment_status)
    if request.method == 'POST':
        form = ShipmentStatusForm(request.POST, instance=shipment_status )
        if form.is_valid():
            form.save()
            return redirect('add_shipment_status')
        
    return render(request, 'dashboard/update/status.html', {"form": form,})



def delete_status(request, id):
    status = get_object_or_404(ShipmentStatus, id=id)
    status.delete()
    return redirect('add_shipment_status')



# ----------------------------------------end------------------------------------------------------------