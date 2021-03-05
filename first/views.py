from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from first.models import Vehicle
from first.templates.forms import New_vehicle

"""Her sjekker `IsAuthenticated` at Token som blir gitt er i databasen. 
Og retunerer en json liste med kjoretoy som er implementert"""
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def home(request):
    data = list(Vehicle.objects.values())
    return JsonResponse({'data': data})

    # vehicles = Vehicle.objects.all()
    # return render(request, "home.html", {'vehicles': vehicles})


def add_vehicle(request):
    new_vehicle = New_vehicle()
    if request.method == 'POST':
        new_vehicle = New_vehicle(request.POST)
        if new_vehicle.is_valid():
            new_vehicle.save()
            return redirect('/')
    context = {'new_vehicle': new_vehicle}
    return render(request, "add_vehicle.html", context)


def update_vehicle(request, pk):
    new_vehicle = Vehicle.objects.get(id=pk)
    up_vehicle = New_vehicle(instance=new_vehicle)
    if request.method == 'POST':
        new_vehicle = New_vehicle(request.POST, request.FILES, instance=new_vehicle)
        if new_vehicle.is_valid():
            new_vehicle.save()
            return redirect('/')
    context = {'new_vehicle': up_vehicle}
    return render(request, "add_vehicle.html", context)


def delete_vehicle(request, pk):
    new_vehicle = Vehicle.objects.get(id=pk)
    if request.method == 'POST':
        new_vehicle.delete()
        return redirect('/')
    context = {'item': new_vehicle}
    return render(request, 'delete.html', context)
