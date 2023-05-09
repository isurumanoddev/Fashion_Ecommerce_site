from store import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('store/', views.store, name="store"),

    path('user_login/', views.user_login, name="user-login"),

]
