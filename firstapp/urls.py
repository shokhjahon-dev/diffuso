from django.urls import path
from .views import index, contact, portfolio, service, about

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('portfolio/', portfolio, name="portfolio"),
    path('service/', service, name="service"),
]