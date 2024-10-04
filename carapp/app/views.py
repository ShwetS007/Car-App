from django.shortcuts import render, redirect
from .models import *
from .forms import*
# Create your views here.
def index(request):
    return render(request, 'index.html')

def cardetail(request):
    car_details = Cars.objects.all()
    return render(request, 'cardetails.html',{'car_details':car_details})

def addcar(request):
    if request.method == 'POST':
            form = CarForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('index')  # Redirect to the homepage after saving
    else:
        form = CarForm()
        return render(request, 'add_car.html', {'form': form})
