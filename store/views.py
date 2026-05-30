from django.shortcuts import render
import requests


def home(request):
    url = "https://dummyjson.com/products"
    response = requests.get(url)
    data = response.json()
    products = data['products']

    return render(request, 'store/home.html', {'products': products})


def store(request):
    url = "https://dummyjson.com/products"
    response = requests.get(url)
    data = response.json()
    products = data['products']

    return render(request, 'store/store.html', {'products': products})


def product_detail(request, id):
    url = f"https://dummyjson.com/products/{id}"
    response = requests.get(url)
    product = response.json()

    return render(request, 'store/product_details.html', {'product': product})


def cart(request):
    return render(request, 'store/cart.html')


def checkout(request):
    return render(request, 'store/checkout.html')


def login(request):
    return render(request, 'store/login.html')


def signup(request):
    return render(request, 'store/signup.html')