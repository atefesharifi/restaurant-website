from django.shortcuts import render
from .models import Food

def food_list(request):
    food_list = Food.objects.all()
    return render(request, "foods/list.html", {'foods':food_list})

def food_detail(request, id):
    food = Food.objects.get(id=id)
    context = {
        "food":food
    }
    return render(request, "foods/detail.html", context)
