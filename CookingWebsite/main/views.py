from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(response):
    return render(response, "main/home.html")

def daily_recipes_breakfast_view(response):
    return render(response, "main/DailyBreakfast.html")

def daily_recipes_lunch_view(response):
    return render(response, "main/DailyLunch.html")

def holidays_view(response):
    return HttpResponse("<h1>This is the holidays page<h1>")