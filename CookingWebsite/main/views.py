from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(response):
    return render(response, "home.html")

def daily_recipes_view(response):
    return HttpResponse("<h1>This is the daily recipes page<h1>")

def holidays_view(response):
    return HttpResponse("<h1>This is the holidays page<h1>")