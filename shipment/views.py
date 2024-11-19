from django.shortcuts import render, redirect, get_object_or_404
from .forms import ShipmentCategoryForm, ShipmentTagsForm, ClientForm, AgentForm, ShipmentForm, ShipmentHistoryFormSet, PackageForm, ShipmentHistoryFormMain
from .models import Shipment_Category, Shipment_Tags, Client, Agent, Shipment, Shipmemt_history, Package
from django.db.models import Q
from cargo.models import Cargo, ShipmentLocation
from django.http import JsonResponse, HttpResponseNotAllowed
from django.forms import inlineformset_factory



def dashboard(request):
	shipment = Shipment.objects.all()
	shipment_count = Shipment.objects.filter(publish="yes").count()
	client_count = Client.objects.all().count()
	location = ShipmentLocation.objects.all().count()
	context = {
	'shipment': shipment,
	'shipment_count' : shipment_count,
	'client_count': client_count,
	'location': location
	}
	return render(request, 'dashboard/index.html', context)


def add_category(request):
	cat_list = Shipment_Category.objects.all()
	if request.method == 'POST':
		form = ShipmentCategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add-category')
	else:
		form = ShipmentCategoryForm()
	return render(request, 'dashboard/add_category.html', {"form": form, "cat_list": cat_list})




def add_tags(request):
	tag_list = Shipment_Tags.objects.all()
	if request.method == 'POST':
		form = ShipmentTagsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_tags')
	else:
		form = ShipmentTagsForm()
	return render(request, 'dashboard/tags.html', {"form": form, "tag_list": tag_list})


def add_clients(request):
	client_list = Client.objects.all()
	if request.method == 'POST':
		form = ClientForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_clients')
	else:
		form = ClientForm()
	return render(request, 'dashboard/add_clients.html', {"form": form, "client_list": client_list})



def agent(request):
	agent_list = Agent.objects.all()
	if request.method == 'POST':
		form = AgentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('add_agent')
	else:
		form = AgentForm()
	return render(request, 'dashboard/add_agent.html', {"form": form, "agent_list": agent_list})



def add_shipment(request):
	errors = ""
	shipment_form = ShipmentForm()
	history_form = ShipmentHistoryFormMain()
	package_form = PackageForm()

	if request.method == 'POST':
		shipment_form = ShipmentForm(request.POST, request.FILES)
		history_form = ShipmentHistoryFormMain(request.POST)
		package_form = PackageForm(request.POST)

		if shipment_form.is_valid() and history_form.is_valid() and package_form.is_valid():
			shipment = shipment_form.save()
			history = history_form.save(commit=False)
			history.shipment = shipment
			history.save()
			package = package_form.save(commit=False)
			package.shipment = shipment
			package.save()
			return redirect('shipment_list')  # Replace with your redirect URL

	context = {
        'shipment_form': shipment_form,
        'history_form': history_form,
        'package_form': package_form,
    }

	return render(request, 'dashboard/add_shipment.html', context)



def shipment_list(request):
	shipment = Shipment.objects.all()
	context = {
	'shipment': shipment,
	}
	return render(request, 'dashboard/shipment-list.html', context)


# def add_status(request):
#     if request.method == 'POST':
#         shipment_id = request.POST.get('shipment_id')
#         status_form = ShipmemtHistoryForm(request.POST)
        
#         if status_form.is_valid():
#             shipment = Shipment.objects.filter(id=shipment_id).first()
            
#             if shipment:
#                 status_obj = status_form.save(commit=False)
#                 status_obj.shipment = shipment
#                 status_obj.save()
                
#                 return redirect('shipment_list')
#             else:
#                 error = 'Shipment does not exist'
#                 # Handle the case where the shipment is not found
#                 return redirect('shipment_list')
        
#         # Handle the case where the form data is invalid
#         else:
#             error = 'Invalid form submission'
#             return redirect('shipment_list')
    
#     # Handle the case where the request method is not POST
#     return render(request, 'dashboard/shipment-list.html', context)





def shipment_update_view(request, id):
    shipment = get_object_or_404(Shipment, pk=id)
    shipment_form = ShipmentForm(instance=shipment)
    package = shipment.shipment_package.first()
    package_form = PackageForm(instance=package)
    ShipmentHistoryFormSet = inlineformset_factory(Shipment, Shipmemt_history, form=ShipmentHistoryFormMain, extra=1, can_delete=True)
    shipment_history_formset = ShipmentHistoryFormSet(instance=shipment)

    if request.method == 'POST':
        shipment_form = ShipmentForm(request.POST, instance=shipment)
        package_form = PackageForm(request.POST, instance=package)
        shipment_history_formset = ShipmentHistoryFormSet(request.POST, instance=shipment)

        if shipment_form.is_valid() and package_form.is_valid() and shipment_history_formset.is_valid():
            shipment = shipment_form.save()
            package = package_form.save()
            shipment_history_formset.save()
            return redirect('shipment_list')  # Replace with your redirect URL

    context = {
        'shipment_form': shipment_form,
        'package_form': package_form,
        'shipment_history_formset': shipment_history_formset,
    }

    return render(request, 'dashboard/update-shipment.html', context)




def delete_shipment(request, shipment_id):
	shipment = get_object_or_404(Shipment, id=shipment_id)
	shipment.delete()
	return redirect('shipment_list')



def tracking(request):
	query = request.GET.get('track-id')
	results = Shipment.objects.filter(Q(tracking_no__iexact=query))
	cargo = Cargo.objects.get(id=1)
	context = {
	'results': results, 
	'cargo': cargo
	}
	return render(request, 'tracking/track.html', context)
