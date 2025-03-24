from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, RecipeForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .models import Recipe

# Create your views here.
#Function that will return the home.html template and render it to the browser
def home_view(request):
    return render(request, "main/home.html")

#Function that will return the DailyBreakfast.html template and render it to the browser
def daily_recipes_breakfast_view(request):
    return render(request, "main/DailyBreakfast.html")

#Function that will return the DailyLunch.html template and render it to the browser
def daily_recipes_lunch_view(request):
    return render(request, "main/DailyLunch.html")

#Function that will return the DailyDinner.html template and render it to the browser
def daily_recipes_dinner_view(request):
    return render(request, "main/DailyDinner.html")

#Function that will return the Holidays.html template and render it to the browser
def holidays_view(request):
    return HttpResponse("<h1>This is the holidays page<h1>")

#Function that will return the Login.html template and render it to the browser
#if the user submits the form, it will validate the details and log in
def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('TCC-home')
        else:
            messages.success(request, ("Your details were incorrect or no such account exists."))
            return redirect('TCC-login')
    else:
        return render(request, "main/Login.html")
    
#Function that will log out the user, display a message and render the login page
def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out."))
    return redirect('TCC-login')

#Function that will return the Register.html template and render it to the browser
def register_view(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,("Your account has been created! Log in below."))
            return redirect('TCC-login')
    else:
        form = RegisterUserForm()

    return render(request, 'main/Register.html', {'form': form})

def recipe_book_view(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            messages.success(request,("Your recipe has been added! Well done Chef."))
            return redirect('recipe-book')
        else:
            messages.success(request, ("Your details were incorrect"))
            return redirect('recipe-book')
    else:
        form = RecipeForm()

    #for logged-in users, fetch their recipes
    if request.user.is_authenticated:
        user_recipes = Recipe.objects.filter(user=request.user)
    #No recipes are fetched for non-logged-in users
    else:
        user_recipes = []

    return render(request, 'main/RecipeBook.html', {'form': form, 'recipes': user_recipes})

def edit_recipe_view(request, recipe_id):
    recipe = Recipe.objects.get(id = recipe_id)
    form = RecipeForm(request.POST, request.FILES, instance=recipe or None)
    if form.is_valid():
        form.save()
        messages.success(request,("Voilà! Your recipe has been updated."))
        return redirect('recipe-book')
    else:
        form = RecipeForm(instance = recipe)

    return render(request, 'main/EditRecipe.html', {'form': form,'recipe': recipe})