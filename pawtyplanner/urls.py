from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path

from pawtyplannerbackend import views


urlpatterns = [
    # url(r'', views.home),
    path('pawtyplannerbackend/', include('pawtyplannerbackend.urls')),
    url(r'^api/public/', views.public),
    url(r'^api/private/', views.private),
    url(r'admin/', admin.site.urls)
]


