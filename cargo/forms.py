from django import forms
from .models import (
    ShipmentMethod,
    ShipmentMode,
    ShipmentLocation,
    ShipmentCarrier,
    PaymentMethod,
    ShipmentStatus,
    Cargo,
)
from django.contrib.auth.forms import AuthenticationForm




class UserForm(AuthenticationForm):
    pass


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'


class ShipmentMethodForm(forms.ModelForm):
    class Meta:
        model = ShipmentMethod
        fields = '__all__'

class ShipmentModeForm(forms.ModelForm):
    class Meta:
        model = ShipmentMode
        fields = '__all__'


class ShipmentLocationForm(forms.ModelForm):
    class Meta:
        model = ShipmentLocation
        fields = '__all__'


class ShipmentCarrierForm(forms.ModelForm):
    class Meta:
        model = ShipmentCarrier
        fields = '__all__'


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = '__all__'


class ShipmentStatusForm(forms.ModelForm):
    class Meta:
        model = ShipmentStatus
        fields = '__all__'