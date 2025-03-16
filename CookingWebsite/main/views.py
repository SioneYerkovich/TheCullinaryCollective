from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from .forms import MemberForm

# Create your views here.
#Function that will return the home.html template and render it to the browser
def home_view(response):
    return render(response, "main/home.html")

#Function that will return the DailyBreakfast.html template and render it to the browser
def daily_recipes_breakfast_view(response):
    return render(response, "main/DailyBreakfast.html")

#Function that will return the DailyLunch.html template and render it to the browser
def daily_recipes_lunch_view(response):
    return render(response, "main/DailyLunch.html")

#Function that will return the DailyDinner.html template and render it to the browser
def daily_recipes_dinner_view(response):
    return render(response, "main/DailyDinner.html")

#Function that will return the Holidays.html template and render it to the browser
def holidays_view(response):
    return HttpResponse("<h1>This is the holidays page<h1>")

#Function that will return the Login.html template and render it to the browser
def login_view(response):
    return render(response, "main/Login.html")

#Function that will return the Register.html template and render it to the browser
def register_view(response):
    if response.method == "POST":
        form = MemberForm(response.POST or None)
        if form.is_valid():
            form.save()
        return render(response, "main/Login.html")
    else:
        return render(response, "main/Register.html")