from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from store.models import *


def user_login(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)

        except:
            print("user not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        print(username, password)
    context = {}
    return render(request, "login_form.html", context)


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

    context = {"products": products}
    return render(request, "store.html", context)


def new_arrivals(request):
    context = {}
    return render(request, "login_form.html", context)
