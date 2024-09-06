from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views, sitemaps

sitemaps = {
    'static': sitemaps.StaticViewSitemap,
}

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
    path('robots.txt', views.robots_txt),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]