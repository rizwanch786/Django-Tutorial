from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name = 'home'),
    path('contact/', contact, name = 'contact-us'),
    path('about/', about, name = 'about-us'),
    path('dynamic/<slug>', dynamic_urls, name = 'dynamic'),
]
