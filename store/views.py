from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from store.models import *
from .forms import CreateUserForm


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
        else:
            print("Login fail")

    context = {}
    return render(request, "login_form.html", context)


def user_register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            Customer.objects.create(
                user=user,
                name=request.POST.get("username"),
                email=request.POST.get("email")
            )

            login(request, user)
            return redirect("home")
    return render(request, "register_form.html")


def user_logout(request):
    logout(request)
    return redirect("home")


def home(request):
    context = {}
    return render(request, "index.html", context)


@login_required(login_url="user-login")
def cart(request):
    customer = request.user.customer
    order,created = Order.objects.get_or_create(customer=customer,complete=False)
    cart_items = order.orderitem_set.all()
    context = {"cart_items":cart_items,"order":order}
    return render(request, "cart.html", context)

def checkout(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    cart_items = order.orderitem_set.all()
    context = {"cart_items": cart_items, "order": order}
    return render(request, "checkout.html", context)
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
