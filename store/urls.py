from store import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('store/', views.store, name="store"),
    path('new_arrivals/', views.new_arrivals, name="new-arrivals"),

    path('user_login/', views.user_login, name="user-login"),
    path('user_register/', views.user_register, name="user-register"),
    path('user_logout/', views.user_logout, name="user-logout"),

]
