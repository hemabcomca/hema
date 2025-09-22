from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('products/', views.products, name='products'),
]
