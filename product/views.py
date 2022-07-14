from django.shortcuts import render, HttpResponse
from .models import Vegetables


def homepage(request):
    products = Vegetables.objects.all() # return list
    context = {"all_vegetables": products}
    return render(request, "product_list.html", context=context)


def pomidor(request):
    pomidor_object = Vegetables.objects.get(id=2)
    pomidor = f"{pomidor_object.name} {pomidor_object.description}"
    return HttpResponse(pomidor)