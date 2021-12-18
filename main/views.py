from django.shortcuts import render
from .models import *


def index(request):
    data = request.POST
    # name = data.get("name")
    # quantity = int(data.get("quantity"))
    # price = float(data.get("price"))
    # Order.objects.create(name=name, quantity=quantity, price=price)
    context = {
        "chicken": Menu.objects.filter(category="chicken"),
        "meat": Menu.objects.filter(category="meat"),
        "menus": Menu.objects.all()
    }
    # print(Menu.objects.filter(category="chicken"))
    return render(request, "index.html", context)


def receipt(request):
    context = {
        "orders": Order.objects.all()
    }
    # request.POST
    # if request.POST:
    #     pass
    #     # Order.objects.filter(name=)

    return render(request, "receipt.html", context)
