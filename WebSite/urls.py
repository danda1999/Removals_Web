from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('Contacts/', views.Contacts, name='Contacts'),
    path('AutoLocksmith/', views.AutoLocksmith, name='AutoLocksmith'),
    path('Removals&Storage/', views.Removals_and_Storage, name='Removals & Storage'),
    path('Cleaning/', views.Cleaning, name='Cleaning'),
    path('Plumbing/', views.Plumbing, name='Plumbing'),
    path('WasteRemovals/', views.Waste_Removals, name='Waste Removals'),
    path('Gardening/', views.Gardening, name='Gardening'),
    path('ElectricalServices/', views.Electrical, name='Electrical Services'),
    path('Landscaping/', views.Landscaping, name='Landscaping'),
    path('Refurbishment/', views.Refurbishment, name='Refurbishment'),
    path('LCE/', views.LCE, name='LCE'),
]