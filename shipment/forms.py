from django import forms
from django.forms import DateInput
from django.forms import TimeInput
from cargo.models import Cargo
import random
import string
from .models import Shipment_Category, Shipment_Tags, Client, Agent, Shipment, Shipmemt_history, Package
from django.forms import inlineformset_factory

class ShipmentCategoryForm(forms.ModelForm):
    class Meta:
        model = Shipment_Category
        fields = ['name', 'description']


class ShipmentTagsForm(forms.ModelForm):
    class Meta:
        model = Shipment_Tags
        fields = ['name', 'description']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['First_Name', 'Last_Name', 'website', 'email']



class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['First_Name', 'Last_Name', 'website', 'email']




class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ShipmentForm(forms.ModelForm):
    pickup_date = forms.DateField(widget=DateInput())
    pickup_time = forms.TimeField(widget=TimeInput())
    departure_time = forms.TimeField(widget=TimeInput())
    expected_delivery_date = forms.DateField(widget=DateInput())
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 2,  # Number of visible rows
        'cols': 40,  # Number of visible columns
        'class': 'custom-textarea',  # CSS class for styling
        'placeholder': 'Enter your text here',  # Placeholder text
    }))

    def clean_tracking_no(self):
        tracking_no = self.cleaned_data.get('tracking_no')
        
        # Check if a tracking with the same tracking_no already exists
        if Shipment.objects.filter(tracking_no=tracking_no).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("A tracking with this tracking number already exists.")
        
        return tracking_no

    class Meta:
        model = Shipment
        fields = [
            'tracking_no', 'shipper_name', 'shipper_phone', 
            'shipper_address', 'shipper_email',
            'receivers_name', 'receivers_phone',
            'receivers_address', 'receivers_email',
            'shipment_method', 'weight', 'package',
            'product', 'payment_mode', 'carrier',
            'departure_time', 'destination', 'pickup_time',
            'comment', 'courier_name', 'mode', 'quantity',
            'carrier_reference_no', 'origin',
            'pickup_date', 'expected_delivery_date', 'feature_image',
            'category', 'tags', 'shipment_client', 'shipment_agent',
            'publish', 
            'total_frieght',
        ]



class ShipmentHistoryForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}))
    remark = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 1,
        'cols': 40,
        'class': 'custom-textarea',
        'placeholder': 'Enter your text here',
    }))

    class Meta:
        model = Shipmemt_history  # Correct model name here
        fields = ['lacation', 'status', 'remark', 'date', 'time', 'updated_by']  # Ensure 'location' is spelled correctly

# Formset should be outside the form class
ShipmentHistoryFormSet = inlineformset_factory(
    Shipment, Shipmemt_history, form=ShipmentHistoryForm, extra=1, can_delete=True
)




class PackageForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 1,  # Number of visible rows
        'cols': 20,  # Number of visible columns
        'class': 'custom-textarea',  # CSS class for styling
        'placeholder': 'Enter your text here',  # Placeholder text
    }))
    class Meta:
        model = Package
        fields = ['quantity', 'Piece_type', 'description', 'length', 'width', 'weight', 'height', 'value']



class ShipmentHistoryFormMain(forms.ModelForm):
    date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}))
    remark = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 1,
        'cols': 40,
        'class': 'custom-textarea',
        'placeholder': 'Enter your text here',
    }))

    class Meta:
        model = Shipmemt_history  # Correct model name here
        fields = ['lacation', 'status', 'remark', 'date', 'time', 'updated_by']  # Ensure 'location' is spelled correctly