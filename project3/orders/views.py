from django.http import HttpResponse
from django.shortcuts import render
from .models import Pizza, Sub, Dinner

# Create your views here.
def index(request):
    return render(request, "orders/index.html")

def menu(request):
    context = {
        "pizzas": Pizza.objects.all(),
        "subs": Sub.objects.all(),
        "dinners": Dinner.objects.all(),
    }
    return render(request, "orders/menu.html", context)