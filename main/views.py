from django.shortcuts import render, HttpResponseRedirect
from .models import *
import math


def index(request):
    data = request.POST
    print(data)
    name = data.get("name")
    quantity = data.get("quantity")
    price = data.get("price")
    if request.method == "POST":
        if name and quantity and price:
            Order.objects.create(name=name, quantity=quantity, price=float(price) * int(quantity))
            Calc.objects.create(name=name, price=price)
    context = {
        "chicken": Menu.objects.filter(category="chicken"),
        "meat": Menu.objects.filter(category="meat"),
        "fries": Menu.objects.filter(category="fries"),
        "menus": Menu.objects.all(),

    }
    return render(request, "index.html", context)


def receipt(request):

    print("____________")
    print(Calc.objects.all())

    Tlist = []
    for i in Calc.objects.all():
        print(i.price)
        Tlist.append(i.price)
        print(Tlist)

    t = math.fsum(Tlist)

    print(t)

    Calc.objects.update(total=t)
    name = request.POST.get("name")
    price = request.POST.get("price")
    if request.method == "POST":
        Calc.objects.update(total= float(t) - float(price))
        Order.objects.filter(name=name).delete()
        Calc.objects.filter(name=name).delete()
    context = {
        "orders": Order.objects.all(),
        "order": Order.objects.count(),
        "total": Calc.objects.last()

    }
    return render(request, "receipt.html", context)
