from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, RecipeForm
from django.contrib.auth import views as auth_views
from .models import Recipe

# Create your views here.
#Function that will return the home.html template and render it to the browser
def home_view(request):
    return render(request, "main/home.html")

#Function that will return the DailyBreakfast.html template, fetch relevant recipes and render it to the browser
def daily_recipes_breakfast_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Breakfast")
    return render(request, "main/DailyBreakfast.html", {'recipes': fetchRecipes})

#Function that will return the DailyLunch.html template, fetch relevant recipes from admin and render it to the browser
def daily_recipes_lunch_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Lunch")
    return render(request, "main/DailyLunch.html", {'recipes': fetchRecipes})

#Function that will return the DailyDinner.html template, fetch relevant recipes from admin and render it to the browser
def daily_recipes_dinner_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Dinner")
    return render(request, "main/DailyDinner.html", {'recipes': fetchRecipes})

#Function that will return the DailyDessert.html template, fetch relevant recipes from admin and render it to the browser
def daily_recipes_dessert_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Dessert")
    return render(request, "main/DailyDessert.html", {'recipes': fetchRecipes})

#Function that will return the DailyDrinks.html template, fetch relevant recipes from admin and render it to the browser
def daily_recipes_drinks_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Drinks")
    return render(request, "main/DailyDrinks.html", {'recipes': fetchRecipes})

#Function that will return the H&DVegetarian.html template, fetch relevant recipes from admin and render it to the browser
def health_recipes_vegetarian_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Vegetarian")
    return render(request, "main/H&DVegetarian.html", {'recipes': fetchRecipes})

#Function that will return the H&DKeto.html template, fetch relevant recipes from admin and render it to the browser
def health_recipes_keto_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Keto")
    return render(request, "main/H&DKeto.html", {'recipes': fetchRecipes})

#Function that will return the HolidaysMD.html template, fetch relevant recipes from admin and render it to the browser
def holidays_md_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Mothers day")
    return render(request, "main/HolidaysMD.html", {'recipes': fetchRecipes})

#Function that will return the HolidaysNY.html template, fetch relevant recipes from admin and render it to the browser
def holidays_ny_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "The New Year")
    return render(request, "main/HolidaysNY.html", {'recipes': fetchRecipes})

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
            messages.error(request, ("Your details were incorrect or no such account exists."))
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
            messages.error(request, ("Sacré bleu! Some of your details were incorrect. Try again."))
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

def delete_recipe_view(request, recipe_id):
    recipe = Recipe.objects.get(id = recipe_id)
    recipe.delete()
    messages.success(request,("The best recipes come from experimentation. Your recipe has been deleted."))
    return redirect('recipe-book')

def search_recipe_view(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        results = Recipe.objects.filter(Name__contains = searched)
        return render(request, 'main/Search.html', {'searched': searched, 'results' : results})
    else:
        return render(request, 'main/Search.html', {})