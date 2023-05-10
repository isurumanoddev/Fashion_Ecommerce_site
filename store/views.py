from django.shortcuts import render
from store.models import *


def home(request):
    context = {}
    return render(request, "index.html", context)


def cart(request):
    context = {}
    return render(request, "cart.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context)


def store(request):
    products = Product.objects.all()

    context = {"products":products}
    return render(request, "store.html", context)


def user_login(request):
    context = {}
    return render(request, "login_form.html", context)


def new_arrivals(request):
    context = {}
    return render(request, "login_form.html", context)
