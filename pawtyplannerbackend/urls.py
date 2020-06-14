from django.conf.urls import url
from pawtyplannerbackend import views

app_name = 'pawtyplannerbackend'

urlpatterns = [
    url(r'home/', views.home, name='home'),
    url(r'buy/', views.buy, name='buy'),
    url(r'gallery/', views.gallery, name='gallery'),
    url(r'contact/', views.contact, name='contact'),
    url(r'checkout/', views.checkout, name='checkout')
]