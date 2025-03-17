from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

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
    if response.method == 'POST':
        username = response.POST["username"]
        password = response.POST["password"]
        user = authenticate(response, username=username, password=password)
        if user is not None:
            login(response, user)
            return redirect('TCC-home')
        else:
            messages.success(response, ("Your details were incorrect or no such account exists."))
            return redirect('TCC-login')
    else:
        return render(response, "main/Login.html")
    
def logout_user(response):
    logout(response)
    messages.success(response, ("You have been logged out."))
    return redirect('TCC-login')

#Function that will return the Register.html template and render it to the browser
def register_view(response):
    if response.method == 'POST':
        form = RegisterUserForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response,("Your account has been created! Log in below."))
            return redirect('TCC-login')
    else:
        form = RegisterUserForm()

    return render(response, 'main/Register.html', {'form': form})