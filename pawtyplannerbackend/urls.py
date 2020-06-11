from django.conf.urls import url
from pawtyplannerbackend import views

app_name = 'pawtyplannerbackend'

urlpatterns = [
    url(r'', views.index),
]