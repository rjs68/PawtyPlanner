from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse


def home(request):
    return render(request, 'pawtyplannerbackend/home.html')


def buy(request):
    return render(request, 'pawtyplannerbackend/buy.html')


def gallery(request):
    return render(request, 'pawtyplannerbackend/gallery.html')


def contact(request):
    return render(request, 'pawtyplannerbackend/contact.html')


def checkout(request):
    return render(request, 'pawtyplannerbackend/checkout.html')


def public(request):
    return HttpResponse("You don't need to be authenticated to see this")


@api_view(['GET'])
def private(request):
    return HttpResponse("You should not see this message if not authenticated!")
