from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('contact/', views.ContactView, name='contact'),
    path('contact/success/', views.SuccessView, name='contact-success')
]
