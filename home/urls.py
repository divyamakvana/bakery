from . import views
from django.urls import path 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('home/products/<int:myid>/', views.productView, name="ProductView"),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('home/checkout/', views.checkout, name='checkout'),
   
    


]