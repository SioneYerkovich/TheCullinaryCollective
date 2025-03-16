from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

# Create your views here.
def home_view(response):
    return render(response, "main/home.html")

def daily_recipes_breakfast_view(response):
    return render(response, "main/DailyBreakfast.html")

def daily_recipes_lunch_view(response):
    return render(response, "main/DailyLunch.html")

def daily_recipes_dinner_view(response):
    return render(response, "main/DailyDinner.html")

def holidays_view(response):
    return HttpResponse("<h1>This is the holidays page<h1>")

def login_view(response):
    return render(response, "main/Login.html")