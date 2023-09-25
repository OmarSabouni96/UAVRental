# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import UAV, UAVRental
from .forms import UAVForm, RentalForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages




def UAVList(request):
    uavs = UAV.objects.all()    
    return render(request, 'uav/uav_list.html', {'uavs': uavs})

def UAVListApi(request):
    return render(request, 'uav/uav_list_api.html')


@login_required(login_url='login')
def UAVCreate(request):
    user_id = request.user.id  # Get the user ID of the logged-in user
    if request.method == 'POST':
        form = UAVForm(request.POST)
        if form.is_valid():
            uav = form.save(commit=False)
            uav.user_id = user_id
            form.save()
            return redirect('uav_list')
    else:
        form = UAVForm()
    return render(request, 'uav/uav_form.html', {'form': form})

def UAVCreateApi(request):
    return render(request, 'uav/uav_form_api.html')


@login_required(login_url='login')
def UAVUpdate(request, pk):
    uav = get_object_or_404(UAV, pk=pk)
    if request.method == 'POST':
        form = UAVForm(request.POST, instance=uav)
        if form.is_valid():
            form.save()
            return redirect('uav_list')
    else:
        form = UAVForm(instance=uav)
    return render(request, 'uav/uav_form.html', {'form': form})

@login_required(login_url='login')
def UAVDelete(request, pk):
    uav = get_object_or_404(UAV, pk=pk)
    if request.method == 'POST':
        uav.delete()
        return redirect('uav_list')
    return render(request, 'uav/uav_confirm_delete.html', {'uav': uav})


# def rental_list(request, pk):
#     uav = get_object_or_404(UAV, pk=pk)  # Get the UAV object by its primary key
#     rentals = UAVRental.objects.filter(uav=uav)  # Retrieve all rentals associated with the UAV

#     return render(request, 'uav/rental_list.html', {'rentals': rentals})

def rental_list(request, pk):
    username = request.GET.get('username')  # Get the username from the form input
    uav = get_object_or_404(UAV, pk=pk)  # Get the UAV object by its primary key
    rentals = UAVRental.objects.filter(uav=uav)  # Retrieve all rentals associated with the UAV

    if username:
        # Filter rental records by username if username is provided
        rentals = rentals.filter(user__username__icontains=username)

    return render(request, 'uav/rental_list.html', {'rentals': rentals})



def rental_list_user(request):
    user_id = request.user.id  # Get the user ID of the logged-in user
    rentals_user = UAVRental.objects.filter(user_id=user_id)  # Retrieve all rentals associated with the UAV
    return render(request, "uav/rentals_user.html", {'rentals_user': rentals_user})


def create_rental(request, pk):
    uav = get_object_or_404(UAV, pk=pk)  # Get the UAV object by its primary key

    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            # Create a new UAVRental record
            rental = form.save(commit=False)
            rental.user = request.user  # Assign the current user as the renter
            rental.uav = uav  # Assign the UAV object to the rental

            # Check for overlapping rentals
            overlapping_rentals = UAVRental.objects.filter(
                uav=uav,
                rental_start_date__lte=rental.rental_end_date,
                rental_end_date__gte=rental.rental_start_date
            )

            # print(f"Overlapping Rentals: {overlapping_rentals.exists()}")

            if overlapping_rentals.exists():
                # There are overlapping rentals
                print("Overlapping rentals exist")
                messages.error(request, "This UAV is already rented during the selected date range.")

            else:
                rental.save()
                return redirect(reverse('rental_list', args=[uav.id]))

    else:
        form = RentalForm()

    return render(request, 'uav/rental_form.html', {'form': form})


@login_required(login_url='login')    
def update_rental(request, pk):
    rental = get_object_or_404(UAVRental, pk=pk)

    # Check if the logged-in user owns this rental
    if rental.user != request.user:
        # Handle unauthorized access here, e.g., raise PermissionDenied
        return redirect('rental_list')  # You can redirect to an appropriate page

    if request.method == 'POST':
        form = RentalForm(request.POST, instance=rental)
        if form.is_valid():
            # Update the rental record
            form.save()
            messages.success(request, "Rental record updated successfully.")
            return redirect('rental_list_user')

    else:
        form = RentalForm(instance=rental)

    return render(request, 'uav/rental_form.html', {'form': form, 'rental': rental})


@login_required(login_url='login')
def delete_rental(request, pk):
    rental = get_object_or_404(UAVRental, pk=pk)
    if request.method == 'POST':
        rental.delete()
        return redirect('rental_list_user')
    return render(request, 'uav/rental_confirm_delete.html', {'rental': rental})