from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('store/', views.store, name='store'),

    path('product/<int:id>/', views.product_detail, name='product_detail'),

    path('cart/', views.cart, name='cart'),

    path('checkout/', views.checkout, name='checkout'),

    path('login/', views.login, name='login'),

    path('signup/', views.signup, name='signup'),

]