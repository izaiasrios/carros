from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm

def cars_view(request):
    search = request.GET.get('search', '').strip()

    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')
    else:
        cars = Car.objects.all().order_by('model')

    return render(request, 'cars.html', {'cars': cars})





def new_cars_view(request):
    if request.method == 'POST':
        new_cars_form = CarModelForm(request.POST, request.FILES)
        if new_cars_form.is_valid():
            new_car = new_cars_form.save()
            return redirect('cars_list')
    else:
        new_cars_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form': new_cars_form})
