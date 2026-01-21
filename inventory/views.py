from django.shortcuts import render, get_object_or_404, redirect
from .models import Bike, Enquiry

def home(request):
    bikes = Bike.objects.filter(is_available=True).order_by('-created_at')
    return render(request, 'inventory/home.html', {'bikes': bikes})


def bike_detail(request, bike_id):
    bike = get_object_or_404(Bike, id=bike_id)

    if request.method == 'POST':
        Enquiry.objects.create(
            bike=bike,
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
        )
        return redirect('bike_detail', bike_id=bike.id)

    return render(request, 'inventory/bike_detail.html', {'bike': bike})
