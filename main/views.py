from django.shortcuts import render, HttpResponseRedirect
from .models import *


def index(request):
    if request.method == "POST":
        data = request.POST
        print(data)

        name = data.get("name")
        quantity = data.get("quantity")
        price = data.get("price")
        Order.objects.create(name=name, quantity=quantity, price=price)

        HttpResponseRedirect("home")
    context = {
        "chicken": Menu.objects.filter(category="chicken"),
        "meat": Menu.objects.filter(category="meat"),
        "fries": Menu.objects.filter(category="fries"),
        "menus": Menu.objects.all()
    }
    return render(request, "index.html", context)


def receipt(request):
    context = {
        "orders": Order.objects.all(),
        "order": Order.objects.count()
    }
    data = request.POST.get("name")

    if request.POST:
        Order.objects.filter(name=data).delete()

    return render(request, "receipt.html", context)
