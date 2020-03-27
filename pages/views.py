from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(request.user)
	print(request.META.get("REMOTE_ADDR"))
	return HttpResponse("Home")

def sobre_view(*args, **kwargs):
	print(request.user)
	print(request.META.get("REMOTE_ADDR"))
	return HttpResponse("Sobre")

def contact_view(*args, **kwargs):
	print(request.user)
	print(request.META.get("REMOTE_ADDR"))
	return HttpResponse("Contacto")