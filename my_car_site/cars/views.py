from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Car

# Create your views here.


def list(request):
    all_cars = Car.objects.all()
    context = {
        'all_cars': all_cars,
    }

    return render(request, 'cars/list.html', context=context)


def add(request):
    # print(request.POST) #  <QueryDict: {'csrfmiddlewaretoken': [
    # 'Nw8n87Ihw6WcUZEGfcNdQHSgrpY1rJTdlInAPJkZpsR9Kx11EEkqGLPbn7VAzqNi'], 'brand': ['asas'], 'year': ['123']}>
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        Car.objects.create(brand=brand, year=year)  # after creating record redirect to list view

        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')


def delete(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            Car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print('pk not found!')
            return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/delete.html')
