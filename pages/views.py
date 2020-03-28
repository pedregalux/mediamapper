from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	# print(request.user)
	# print(request.META.get("REMOTE_ADDR"))
	return render(request, "home.html", {})

def sobre_view(request, *args, **kwargs):
	# print(request.user)
	# print(request.META.get("REMOTE_ADDR"))
	return render(request, "sobre.html", {})

def contacto_view(request, *args, **kwargs):
	# print(request.user)
	# print(request.META.get("REMOTE_ADDR"))
	return render(request, "contacto.html", {})