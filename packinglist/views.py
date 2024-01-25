from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip, Item
from django.contrib.auth.models import User
from .forms import TripForm 
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.core.paginator import Paginator


def trip_list(request):
    trip_list = Trip.objects.all()
    paginator = Paginator(trip_list, 5)  # Show 5 trips per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'packinglist/trips.html', {'page_obj': page_obj})

def packinglist(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    items = trip.items.all()
    return render(request, 'packinglist/packinglist.html', {'trip': trip, 'items': items})


def add_item(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        trip_id = request.POST.get('trip_id')
        assigned_to_id = request.POST.get('assigned_to')  # Get the user ID from the form

        trip = get_object_or_404(Trip, id=trip_id)
        assigned_to = get_object_or_404(User, id=assigned_to_id)  # Get the User object

        # Create the Item with assigned_to field set
        Item.objects.create(name=item_name, trip=trip, assigned_to=assigned_to)

        return redirect('packinglist', trip_id=trip.id)

    trips = Trip.objects.all()
    users = User.objects.all()
    return render(request, 'packinglist/add_item.html', {'trips': trips, 'users': users})

def add_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trip_list')
    else:
        form = TripForm()
    return render(request, 'packinglist/add_trip.html', {'form': form})

def dashboard(request):
    # You can pass additional context to the template if needed
    return render(request, 'packinglist/dashboard.html')

def some_protected_view(request):
    # Example view logic
    return render(request, 'registration/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a redirect here to the login page after successful registration
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'packinglist/register.html', {'form': form})