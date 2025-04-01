from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, RecipeForm, ReviewForm
from django.contrib.auth import views as auth_views
from .models import Recipe, Review, Favourite
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
#Function that will return the home.html template and render it to the browser
def home_view(request):
    return render(request, "main/home.html")

#Function that will return the DailyBreakfast.html template, fetch relevant recipes and render it to the browser
def daily_recipes_breakfast_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Breakfast")
    fetchReviews = Review.objects.filter(recipe__in=fetchRecipes)
    if request.user.is_authenticated:
        liked_recipes = request.user.likes.all()
    else:
        liked_recipes = getattr(request.user, 'liked_recipes', None)
    

    return render(request, "main/DailyBreakfast.html", {'recipes': fetchRecipes, 'reviews' : fetchReviews, 'liked_recipes': liked_recipes})

#Function that allows users to like/unlike breakfast recipes and refresh the page
def like_view_breakfast(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to like a recipe.")
        return redirect('TCC-login')
    
    recipe = get_object_or_404(Recipe, id = request.POST.get('recipe_id'))
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        messages.error(request, f"You unliked the recipe: {recipe.Name}. We hope you find something suitable!")
    else:
        recipe.likes.add(request.user)
        messages.success(request, f"You liked the recipe: {recipe.Name}. Thank you for supporting our community!")
    return redirect(daily_recipes_breakfast_view)

#Function that allows users to favourite/unfavourite breakfast recipes and refresh the page
def add_favourite_breakfast(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to favourite a recipe.")
        return redirect('TCC-login')

    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    favorite, created = Favourite.objects.get_or_create(user=request.user, recipe=recipe)
    
    if not created:
        messages.error(request, f"You already have {recipe.Name} in your favorites.")
    else:
        messages.success(request, f"You have added {recipe.Name} to your favorites.")

    return redirect('daily-recipes-breakfast')

#Function that allows users to make reviews for breakfast recipes and refresh the page
def review_breakfast_view(request, recipe_id): 
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to leave a review.")
        return redirect('TCC-login')
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            existing_review = Review.objects.filter(user=request.user, recipe=recipe).first()

            if existing_review:
                messages.error(request, 'You have already reviewed this recipe.')
                return redirect('daily-recipes-breakfast')
            else:
                review = form.save(commit=False)
                review.recipe = recipe
                review.user = request.user
                review.save()
                messages.success(request, 'Your review has been added!')
                return redirect('daily-recipes-breakfast')
        else:
            messages.error(request, 'Please ensure all fields are filled correctly.')
            return redirect('daily-recipes-breakfast')
    
    else:
        form = ReviewForm() 

    return render(request, 'main/Review.html', {'form': form, 'recipe': recipe})

#View to edit a breakfast review
def edit_review_breakfast_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        messages.error(request, "This is not your review to edit.")
        return redirect('daily-recipes-breakfast')

    if request.method == 'POST':
        content = request.POST.get('content')

        if not content.strip():
            messages.error(request, 'Review content cannot be empty.')
            return redirect('edit-review-breakfast', recipe_id=recipe.id, review_id=review.id)

        review.content = content
        review.save()

        messages.success(request, 'Your review has been updated!')
        return redirect('daily-recipes-breakfast')

    return render(request, 'main/EditReview.html', {'review': review, 'recipe': recipe})

#View to delete a breakfast review
def delete_review_breakfast_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id, recipe=recipe)

    if review.user != request.user:
        messages.error(request, "You are not authorized to delete this review.")
        return redirect('daily-recipes-breakfast')

    review.delete()

    messages.success(request, "Your review has been deleted.")
    return redirect('daily-recipes-breakfast')

#Function that will return the DailyLunch.html template, fetch relevant recipes from admin and render it to the browser
def daily_recipes_lunch_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Lunch")
    fetchReviews = Review.objects.filter(recipe__in=fetchRecipes)
    if request.user.is_authenticated:
        liked_recipes = request.user.likes.all()
    else:
        liked_recipes = getattr(request.user, 'liked_recipes', None)
    return render(request, "main/DailyLunch.html", {'recipes': fetchRecipes, 'reviews' : fetchReviews, 'liked_recipes': liked_recipes})

#View to edit a lunch review
def edit_review_lunch_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        messages.error(request, "This is not your review to edit.")
        return redirect('daily-recipes-lunch')

    if request.method == 'POST':
        content = request.POST.get('content')

        if not content.strip():
            messages.error(request, 'Review content cannot be empty.')
            return redirect('edit-review-lunch', recipe_id=recipe.id, review_id=review.id)


        review.content = content
        review.save()

        messages.success(request, 'Your review has been updated!')
        return redirect('daily-recipes-lunch')

    return render(request, 'main/EditReview.html', {'review': review, 'recipe': recipe})

#View to delete a lunch review
def delete_review_lunch_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id, recipe=recipe)

    if review.user != request.user:
        messages.error(request, "You are not authorized to delete this review.")
        return redirect('daily-recipes-lunch')

    
    else:
        review.delete()
        messages.success(request, "Your review has been deleted.")
        return redirect('daily-recipes-lunch')

#Function that allows users to make reviews for lunch recipes and refresh the page
def review_lunch_view(request, recipe_id): 
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to leave a review.")
        return redirect('TCC-login')
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            existing_review = Review.objects.filter(user=request.user, recipe=recipe).first()

            if existing_review:
                messages.error(request, 'You have already reviewed this recipe.')
                return redirect('daily-recipes-breakfast')
            else:
                review = form.save(commit=False)
                review.recipe = recipe
                review.user = request.user
                review.save()
                messages.success(request, 'Your review has been added!')
                return redirect('daily-recipes-breakfast')
        else:
            messages.error(request, 'Please ensure all fields are filled correctly.')
            return redirect('daily-recipes-breakfast')
    
    else:
        form = ReviewForm() 

    return render(request, 'main/Review.html', {'form': form, 'recipe': recipe})

#Function that allows users to like/unlike lunch recipes and refresh the page
def like_view_lunch(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to like a recipe.")
        return redirect('TCC-login')
    
    recipe = get_object_or_404(Recipe, id = request.POST.get('recipe_id'))
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        liked = False
        messages.error(request, f"You unliked the recipe: {recipe.Name}, we hope you find something suitable!")
    else:
        recipe.likes.add(request.user)
        liked = True
        messages.success(request, f"You liked the recipe: {recipe.Name}, thank you for supporting our community!")
    return redirect(daily_recipes_lunch_view)

#Function that allows users to favourite/unfavourite lunch recipes and refresh the page
def add_favourite_lunch(request, recipe_id):  
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to favourite a recipe.")
        return redirect('TCC-login')

    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    favorite, created = Favourite.objects.get_or_create(user=request.user, recipe=recipe)
    
    if not created:
        messages.error(request, f"You already have {recipe.Name} in your favorites.")
    else:
        messages.success(request, f"You have added {recipe.Name} to your favorites.")

    return redirect('daily-recipes-dinner')

#Function that will return the DailyDinner.html template, fetch relevant recipes from admin and render it to the browser
def daily_recipes_dinner_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Dinner")
    fetchReviews = Review.objects.filter(recipe__in=fetchRecipes)
    if request.user.is_authenticated:
        liked_recipes = request.user.likes.all()
    else:
        liked_recipes = getattr(request.user, 'liked_recipes', None)
    return render(request, "main/DailyDinner.html", {'recipes': fetchRecipes, 'reviews' : fetchReviews, 'liked_recipes': liked_recipes})

#Function that allows users to like/unlike dinner recipes and refresh the page
def like_view_dinner(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to like a recipe.")
        return redirect('TCC-login')
    
    recipe = get_object_or_404(Recipe, id = request.POST.get('recipe_id'))
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        liked = False
        messages.error(request, f"You unliked the recipe: {recipe.Name}, we hope you find something suitable!")
    else:
        recipe.likes.add(request.user)
        liked = True
        messages.success(request, f"You liked the recipe: {recipe.Name}, thank you for supporting our community!")
    return redirect(daily_recipes_dinner_view)

#Function that allows users to favourite/unfavourite dinner recipes and refresh the page
def add_favourite_dinner(request, recipe_id):  
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to favourite a recipe.")
        return redirect('TCC-login')

    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    favorite, created = Favourite.objects.get_or_create(user=request.user, recipe=recipe)
    
    if not created:
        messages.error(request, f"You already have {recipe.Name} in your favorites.")
    else:
        messages.success(request, f"You have added {recipe.Name} to your favorites.")

    return redirect('daily-recipes-dinner')

#View to edit a dinner review
def edit_review_dinner_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        messages.error(request, "This is not your review to edit.")
        return redirect('daily-recipes-dinner')

    if request.method == 'POST':
        content = request.POST.get('content')

        if not content.strip():
            messages.error(request, 'Review content cannot be empty.')
            return redirect('edit-review-dinner', recipe_id=recipe.id, review_id=review.id)

        review.content = content
        review.save()

        messages.success(request, 'Your review has been updated!')
        return redirect('daily-recipes-dinner')  # Redirect to the appropriate page

    return render(request, 'main/EditReview.html', {'review': review, 'recipe': recipe})

#View to delete a dinner review
def delete_review_dinner_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id, recipe=recipe)

    if review.user != request.user:
        messages.error(request, "You are not authorized to delete this review.")
        return redirect('daily-recipes-dinner')

    review.delete()

    messages.success(request, "Your review has been deleted.")
    return redirect('daily-recipes-dinner')

#Function that allows users to make reviews for dinner recipes and refresh the page
def review_dinner_view(request, recipe_id): 
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to leave a review.")
        return redirect('TCC-login')
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            existing_review = Review.objects.filter(user=request.user, recipe=recipe).first()

            if existing_review:
                messages.error(request, 'You have already reviewed this recipe.')
                return redirect('daily-recipes-breakfast')
            else:
                review = form.save(commit=False)
                review.recipe = recipe
                review.user = request.user
                review.save()
                messages.success(request, 'Your review has been added!')
                return redirect('daily-recipes-breakfast')
        else:
            messages.error(request, 'Please ensure all fields are filled correctly.')
            return redirect('daily-recipes-breakfast')
    
    else:
        form = ReviewForm() 

    return render(request, 'main/Review.html', {'form': form, 'recipe': recipe})

#Function that will return the DailyDessert.html template, fetch relevant recipes from admin and render it to the browser
def daily_recipes_dessert_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Dessert")
    fetchReviews = Review.objects.filter(recipe__in=fetchRecipes)
    if request.user.is_authenticated:
        liked_recipes = request.user.likes.all()
    else:
        liked_recipes = getattr(request.user, 'liked_recipes', None)
    return render(request, "main/DailyDessert.html", {'recipes': fetchRecipes, 'reviews' : fetchReviews, 'liked_recipes': liked_recipes})

#View to edit a dessert review
def edit_review_dessert_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        messages.error(request, "This is not your review to edit.")
        return redirect('daily-recipes-dessert')

    if request.method == 'POST':
        content = request.POST.get('content')

        if not content.strip():
            messages.error(request, 'Review content cannot be empty.')
            return redirect('edit-review-dessert', recipe_id=recipe.id, review_id=review.id)

        review.content = content
        review.save()

        messages.success(request, 'Your review has been updated!')
        return redirect('daily-recipes-dessert')

    return render(request, 'main/EditReview.html', {'review': review, 'recipe': recipe})

#View to delete a dessert review
def delete_review_dessert_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id, recipe=recipe)

    if review.user != request.user:
        messages.error(request, "You are not authorized to delete this review.")
        return redirect('daily-recipes-dessert')

    review.delete()

    messages.success(request, "Your review has been deleted.")
    return redirect('daily-recipes-dessert')

#Function that allows users to make reviews for dessert recipes and refresh the page
def review_dessert_view(request, recipe_id): 
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to leave a review.")
        return redirect('TCC-login')
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            existing_review = Review.objects.filter(user=request.user, recipe=recipe).first()

            if existing_review:
                messages.error(request, 'You have already reviewed this recipe.')
                return redirect('daily-recipes-breakfast')
            else:
                review = form.save(commit=False)
                review.recipe = recipe
                review.user = request.user
                review.save()
                messages.success(request, 'Your review has been added!')
                return redirect('daily-recipes-breakfast')
        else:
            messages.error(request, 'Please ensure all fields are filled correctly.')
            return redirect('daily-recipes-breakfast')
    
    else:
        form = ReviewForm() 

    return render(request, 'main/Review.html', {'form': form, 'recipe': recipe})

#Function that allows users to like/unlike dessert recipes and refresh the page
def like_view_dessert(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to like a recipe.")
        return redirect('TCC-login')
    
    recipe = get_object_or_404(Recipe, id = request.POST.get('recipe_id'))
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        liked = False
        messages.error(request, f"You unliked the recipe: {recipe.Name}, we hope you find something suitable!")
    else:
        recipe.likes.add(request.user)
        liked = True
        messages.success(request, f"You liked the recipe: {recipe.Name}, thank you for supporting our community!")
    return redirect(daily_recipes_dessert_view)

#Function that allows users to favourite/unfavourite dessert recipes and redirects to the recipe-book
def add_favourite_dessert(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to favourite a recipe.")
        return redirect('TCC-login')

    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    favorite, created = Favourite.objects.get_or_create(user=request.user, recipe=recipe)
    
    if not created:
        messages.error(request, f"You already have {recipe.Name} in your favorites.")
    else:
        messages.success(request, f"You have added {recipe.Name} to your favorites.")

    return redirect('daily-recipes-dessert')

#Function that will return the DailyDrinks.html template, fetch relevant recipes from admin and render it to the browser
def daily_recipes_drinks_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Drinks")
    fetchReviews = Review.objects.filter(recipe__in=fetchRecipes)
    if request.user.is_authenticated:
        liked_recipes = request.user.likes.all()
    else:
        liked_recipes = getattr(request.user, 'liked_recipes', None)
    return render(request, "main/DailyDrinks.html", {'recipes': fetchRecipes, 'reviews' : fetchReviews, 'liked_recipes': liked_recipes})

#View to edit a drinks review
def edit_review_drinks_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        messages.error(request, "This is not your review to edit.")
        return redirect('daily-recipes-drinks')

    if request.method == 'POST':
        content = request.POST.get('content')

        if not content.strip():
            messages.error(request, 'Review content cannot be empty.')
            return redirect('edit-review-drinks', recipe_id=recipe.id, review_id=review.id)


        review.content = content
        review.save()

        messages.success(request, 'Your review has been updated!')
        return redirect('daily-recipes-drinks')

    return render(request, 'main/EditReview.html', {'review': review, 'recipe': recipe})

#View to delete a drinks review
def delete_review_drinks_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id, recipe=recipe)

    if review.user != request.user:
        messages.error(request, "You are not authorized to delete this review.")
        return redirect('daily-recipes-drinks')

    review.delete()

    messages.success(request, "Your review has been deleted.")
    return redirect('daily-recipes-drinks')

#Function that allows users to make reviews for drinks recipes and refresh the page
def review_drinks_view(request, recipe_id): 
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to leave a review.")
        return redirect('TCC-login')
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            existing_review = Review.objects.filter(user=request.user, recipe=recipe).first()

            if existing_review:
                messages.error(request, 'You have already reviewed this recipe.')
                return redirect('daily-recipes-breakfast')
            else:
                review = form.save(commit=False)
                review.recipe = recipe
                review.user = request.user
                review.save()
                messages.success(request, 'Your review has been added!')
                return redirect('daily-recipes-breakfast')
        else:
            messages.error(request, 'Please ensure all fields are filled correctly.')
            return redirect('daily-recipes-breakfast')
    
    else:
        form = ReviewForm() 

    return render(request, 'main/Review.html', {'form': form, 'recipe': recipe})

#Function that allows users to like/unlike drinks recipes and refresh the page
def like_view_drinks(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to like a recipe.")
        return redirect('TCC-login')
    
    recipe = get_object_or_404(Recipe, id = request.POST.get('recipe_id'))
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        liked = False
        messages.error(request, f"You unliked the recipe: {recipe.Name}, we hope you find something suitable!")
    else:
        recipe.likes.add(request.user)
        liked = True
        messages.success(request, f"You liked the recipe: {recipe.Name}, thank you for supporting our community!")
    return redirect(daily_recipes_drinks_view)

#Function that allows users to favourite/unfavourite drinks recipes and redirects to the recipe-book
def add_favourite_drinks(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to favourite a recipe.")
        return redirect('TCC-login')

    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    favorite, created = Favourite.objects.get_or_create(user=request.user, recipe=recipe)
    
    if not created:
        messages.error(request, f"You already have {recipe.Name} in your favorites.")
    else:
        messages.success(request, f"You have added {recipe.Name} to your favorites.")

    return redirect('daily-recipes-drinks')

#Function that will return the H&DVegetarian.html template, fetch relevant recipes from admin and render it to the browser
def health_recipes_vegetarian_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Vegetarian")
    fetchReviews = Review.objects.filter(recipe__in=fetchRecipes)
    if request.user.is_authenticated:
        liked_recipes = request.user.likes.all()
    else:
        liked_recipes = getattr(request.user, 'liked_recipes', None)
    return render(request, "main/H&DVegetarian.html", {'recipes': fetchRecipes, 'reviews' : fetchReviews, 'liked_recipes': liked_recipes})

#View to edit a vegetarian review
def edit_review_vegetarian_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        messages.error(request, "This is not your review to edit.")
        return redirect('health-recipes-vegetarian')

    if request.method == 'POST':
        content = request.POST.get('content')

        if not content.strip():
            messages.error(request, 'Review content cannot be empty.')
            return redirect('edit-review-vegetarian', recipe_id=recipe.id, review_id=review.id)


        review.content = content
        review.save()

        messages.success(request, 'Your review has been updated!')
        return redirect('health-recipes-vegetarian')

    return render(request, 'main/EditReview.html', {'review': review, 'recipe': recipe})

#View to delete a vegetarian review
def delete_review_vegetarian_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id, recipe=recipe)

    if review.user != request.user:
        messages.error(request, "You are not authorized to delete this review.")
        return redirect('health-recipes-vegetarian')

    review.delete()

    messages.success(request, "Your review has been deleted.")
    return redirect('health-recipes-vegetarian')

#Function that allows users to make reviews for vegetarian recipes and refresh the page
def review_vegetarian_view(request, recipe_id): 
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to leave a review.")
        return redirect('TCC-login')
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            existing_review = Review.objects.filter(user=request.user, recipe=recipe).first()

            if existing_review:
                messages.error(request, 'You have already reviewed this recipe.')
                return redirect('daily-recipes-breakfast')
            else:
                review = form.save(commit=False)
                review.recipe = recipe
                review.user = request.user
                review.save()
                messages.success(request, 'Your review has been added!')
                return redirect('daily-recipes-breakfast')
        else:
            messages.error(request, 'Please ensure all fields are filled correctly.')
            return redirect('daily-recipes-breakfast')
    
    else:
        form = ReviewForm() 

    return render(request, 'main/Review.html', {'form': form, 'recipe': recipe})

#Function that allows users to like/unlike vegetarian recipes and refresh the page
def like_view_vegetarian(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to like a recipe.")
        return redirect('TCC-login')
    
    recipe = get_object_or_404(Recipe, id = request.POST.get('recipe_id'))
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        liked = False
        messages.error(request, f"You unliked the recipe: {recipe.Name}, we hope you find something suitable!")
    else:
        recipe.likes.add(request.user)
        liked = True
        messages.success(request, f"You liked the recipe: {recipe.Name}, thank you for supporting our community!")
    return redirect(health_recipes_vegetarian_view)

#Function that allows users to favourite/unfavourite vegetarian recipes and redirects to the recipe-book
def add_favourite_vegetarian(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to favourite a recipe.")
        return redirect('TCC-login')

    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    favorite, created = Favourite.objects.get_or_create(user=request.user, recipe=recipe)
    
    if not created:
        messages.error(request, f"You already have {recipe.Name} in your favorites.")
    else:
        messages.success(request, f"You have added {recipe.Name} to your favorites.")

    return redirect('health-recipes-vegetarian')

#Function that will return the H&DKeto.html template, fetch relevant recipes from admin and render it to the browser
def health_recipes_keto_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Keto")
    fetchReviews = Review.objects.filter(recipe__in=fetchRecipes)
    if request.user.is_authenticated:
        liked_recipes = request.user.likes.all()
    else:
        liked_recipes = getattr(request.user, 'liked_recipes', None)
    return render(request, "main/H&DKeto.html", {'recipes': fetchRecipes, 'reviews' : fetchReviews, 'liked_recipes': liked_recipes})

#View to edit a keto review
def edit_review_keto_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        messages.error(request, "This is not your review to edit.")
        return redirect('health-recipes-keto')

    if request.method == 'POST':
        content = request.POST.get('content')

        if not content.strip():
            messages.error(request, 'Review content cannot be empty.')
            return redirect('edit-review-keto', recipe_id=recipe.id, review_id=review.id)


        review.content = content
        review.save()

        messages.success(request, 'Your review has been updated!')
        return redirect('health-recipes-keto')

    return render(request, 'main/EditReview.html', {'review': review, 'recipe': recipe})

#View to delete a keto review
def delete_review_keto_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id, recipe=recipe)

    if review.user != request.user:
        messages.error(request, "You are not authorized to delete this review.")
        return redirect('health-recipes-keto')

    review.delete()

    messages.success(request, "Your review has been deleted.")
    return redirect('health-recipes-keto')

#Function that allows users to make reviews for keto recipes and refresh the page
def review_keto_view(request, recipe_id): 
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to leave a review.")
        return redirect('TCC-login')
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            existing_review = Review.objects.filter(user=request.user, recipe=recipe).first()

            if existing_review:
                messages.error(request, 'You have already reviewed this recipe.')
                return redirect('daily-recipes-breakfast')
            else:
                review = form.save(commit=False)
                review.recipe = recipe
                review.user = request.user
                review.save()
                messages.success(request, 'Your review has been added!')
                return redirect('daily-recipes-breakfast')
        else:
            messages.error(request, 'Please ensure all fields are filled correctly.')
            return redirect('daily-recipes-breakfast')
    
    else:
        form = ReviewForm() 

    return render(request, 'main/Review.html', {'form': form, 'recipe': recipe})

#Function that allows users to like/unlike keto recipes and refresh the page
def like_view_keto(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to like a recipe.")
        return redirect('TCC-login')
    
    recipe = get_object_or_404(Recipe, id = request.POST.get('recipe_id'))
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        liked = False
        messages.error(request, f"You unliked the recipe: {recipe.Name}, we hope you find something suitable!")
    else:
        recipe.likes.add(request.user)
        liked = True
        messages.success(request, f"You liked the recipe: {recipe.Name}, thank you for supporting our community!")
    return redirect(health_recipes_keto_view)

#Function that allows users to favourite/unfavourite keto recipes and redirects to the recipe-book
def add_favourite_keto(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to favourite a recipe.")
        return redirect('TCC-login')

    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    favorite, created = Favourite.objects.get_or_create(user=request.user, recipe=recipe)
    
    if not created:
        messages.error(request, f"You already have {recipe.Name} in your favorites.")
    else:
        messages.success(request, f"You have added {recipe.Name} to your favorites.")

    return redirect('health-recipes-keto')

#Function that will return the HolidaysMD.html template, fetch relevant recipes from admin and render it to the browser
def holidays_md_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "Mothers day")
    fetchReviews = Review.objects.filter(recipe__in=fetchRecipes)
    if request.user.is_authenticated:
        liked_recipes = request.user.likes.all()
    else:
        liked_recipes = getattr(request.user, 'liked_recipes', None)
    return render(request, "main/HolidaysMD.html", {'recipes': fetchRecipes, 'reviews' : fetchReviews, 'liked_recipes': liked_recipes})

#View to edit a mothers day review
def edit_review_md_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        messages.error(request, "This is not your review to edit.")
        return redirect('holiday-recipes-MD')

    if request.method == 'POST':
        content = request.POST.get('content')

        if not content.strip():
            messages.error(request, 'Review content cannot be empty.')
            return redirect('edit-review-md', recipe_id=recipe.id, review_id=review.id)


        review.content = content
        review.save()

        messages.success(request, 'Your review has been updated!')
        return redirect('holiday-recipes-MD')

    return render(request, 'main/EditReview.html', {'review': review, 'recipe': recipe})

#View to delete a mothers day review
def delete_review_md_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id, recipe=recipe)

    if review.user != request.user:
        messages.error(request, "You are not authorized to delete this review.")
        return redirect('holiday-recipes-MD')

    review.delete()

    messages.success(request, "Your review has been deleted.")
    return redirect('holiday-recipes-MD')

#Function that allows users to make reviews for mothers day recipes and refresh the page
def review_md_view(request, recipe_id): 
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to leave a review.")
        return redirect('TCC-login')
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            existing_review = Review.objects.filter(user=request.user, recipe=recipe).first()

            if existing_review:
                messages.error(request, 'You have already reviewed this recipe.')
                return redirect('daily-recipes-breakfast')
            else:
                review = form.save(commit=False)
                review.recipe = recipe
                review.user = request.user
                review.save()
                messages.success(request, 'Your review has been added!')
                return redirect('daily-recipes-breakfast')
        else:
            messages.error(request, 'Please ensure all fields are filled correctly.')
            return redirect('daily-recipes-breakfast')
    
    else:
        form = ReviewForm() 

    return render(request, 'main/Review.html', {'form': form, 'recipe': recipe})

#Function that allows users to like/unlike mothers day recipes and refresh the page
def like_view_md(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to like a recipe.")
        return redirect('TCC-login')
    
    recipe = get_object_or_404(Recipe, id = request.POST.get('recipe_id'))
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        liked = False
        messages.error(request, f"You unliked the recipe: {recipe.Name}, we hope you find something suitable!")
    else:
        recipe.likes.add(request.user)
        liked = True
        messages.success(request, f"You liked the recipe: {recipe.Name}, thank you for supporting our community!")
    return redirect(holidays_md_view)

#Function that allows users to favourite/unfavourite mothers day recipes and redirects to the recipe-book
def add_favourite_md(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to favourite a recipe.")
        return redirect('TCC-login')

    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    favorite, created = Favourite.objects.get_or_create(user=request.user, recipe=recipe)
    
    if not created:
        messages.error(request, f"You already have {recipe.Name} in your favorites.")
    else:
        messages.success(request, f"You have added {recipe.Name} to your favorites.")

    return redirect('holiday-recipes-MD')

#Function that will return the HolidaysNY.html template, fetch relevant recipes from admin and render it to the browser
def holidays_ny_view(request):
    fetchRecipes = Recipe.objects.filter(user__username = "admin", subcategory__type = "The New Year")
    fetchReviews = Review.objects.filter(recipe__in=fetchRecipes)
    if request.user.is_authenticated:
        liked_recipes = request.user.likes.all()
    else:
        liked_recipes = getattr(request.user, 'liked_recipes', None)
    return render(request, "main/HolidaysNY.html", {'recipes': fetchRecipes, 'reviews' : fetchReviews, 'liked_recipes': liked_recipes})

#View to edit a new years review
def edit_review_ny_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id)

    if review.user != request.user:
        messages.error(request, "This is not your review to edit.")
        return redirect('holiday-recipes-MD')

    if request.method == 'POST':
        content = request.POST.get('content')

        if not content.strip():
            messages.error(request, 'Review content cannot be empty.')
            return redirect('edit-review-ny', recipe_id=recipe.id, review_id=review.id)


        review.content = content
        review.save()

        messages.success(request, 'Your review has been updated!')
        return redirect('holiday-recipes-NY')

    return render(request, 'main/EditReview.html', {'review': review, 'recipe': recipe})

#View to delete a new years review
def delete_review_ny_view(request, recipe_id, review_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    review = get_object_or_404(Review, id=review_id, recipe=recipe)

    if review.user != request.user:
        messages.error(request, "You are not authorized to delete this review.")
        return redirect('holiday-recipes-NY')

    review.delete()

    messages.success(request, "Your review has been deleted.")
    return redirect('holiday-recipes-NY')

#Function that allows users to make reviews for new years recipes and refresh the page
def review_ny_view(request, recipe_id): 
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to leave a review.")
        return redirect('TCC-login')
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            existing_review = Review.objects.filter(user=request.user, recipe=recipe).first()

            if existing_review:
                messages.error(request, 'You have already reviewed this recipe.')
                return redirect('daily-recipes-breakfast')
            else:
                review = form.save(commit=False)
                review.recipe = recipe
                review.user = request.user
                review.save()
                messages.success(request, 'Your review has been added!')
                return redirect('daily-recipes-breakfast')
        else:
            messages.error(request, 'Please ensure all fields are filled correctly.')
            return redirect('daily-recipes-breakfast')
    
    else:
        form = ReviewForm() 

    return render(request, 'main/Review.html', {'form': form, 'recipe': recipe})

#Function that allows users to like/unlike new years recipes and refresh the page
def like_view_ny(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to like a recipe.")
        return redirect('TCC-login')
    
    recipe = get_object_or_404(Recipe, id = request.POST.get('recipe_id'))
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
        liked = False
        messages.error(request, f"You unliked the recipe: {recipe.Name}, we hope you find something suitable!")
    else:
        recipe.likes.add(request.user)
        liked = True
        messages.success(request, f"You liked the recipe: {recipe.Name}, thank you for supporting our community!")
    return redirect(holidays_ny_view)

#Function that allows users to favourite/unfavourite new years recipes and redirects to the recipe-book
def add_favourite_ny(request, recipe_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to favourite a recipe.")
        return redirect('TCC-login')

    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    favorite, created = Favourite.objects.get_or_create(user=request.user, recipe=recipe)
    
    if not created:
        messages.error(request, f"You already have {recipe.Name} in your favorites.")
    else:
        messages.success(request, f"You have added {recipe.Name} to your favorites.")

    return redirect('holiday-recipes-NY')

#Function that will return the Login.html template and render it to the browser
#if the user submits the form, it will validate the details and log in
def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in. Log out using the door in the top right corner.")
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

#Function that will return the RecipeBook.html template and render it to the browser, fetches user favourites and personal recipes
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

    #for logged-in users, fetch their recipes and favourites
    if request.user.is_authenticated:
        user_recipes = Recipe.objects.filter(user=request.user)
        #Get all recipes that the user has favorited
        favourites = Favourite.objects.filter(user=request.user)
        #Fetch the recipes associated with the favorites
        favorite_recipes = [favourite.recipe for favourite in favourites]
        #No recipes are fetched for non-logged-in users
    else:
        favorite_recipes = []
        user_recipes = []

    return render(request, 'main/RecipeBook.html', {'form': form, 'recipes': user_recipes, 'favorite_recipes': favorite_recipes})

#Function that allows users to unfavourite recipes inside of the recipe book and refresh the page
def remove_favourite_recipebook(request, recipe_id):  
    recipe = get_object_or_404(Recipe, id=recipe_id)
    favorite, created = Favourite.objects.get_or_create(user=request.user, recipe=recipe)
    
    if not created:
        favorite.delete()
        messages.error(request, f"You have removed {recipe.Name} from your favorites.")
    
    return redirect('recipe-book')

#Function that allows users to edit recipes from the recipe book, then redirect back to the recipe book
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

#Function that allows users to delete recipes from the recipe book, then redirect back to the recipe book
def delete_recipe_view(request, recipe_id):
    recipe = Recipe.objects.get(id = recipe_id)
    recipe.delete()
    messages.error(request,("The best recipes come from experimentation. Your recipe has been deleted."))
    return redirect('recipe-book')

#Function that allows users to search for recipes
def search_recipe_view(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        results = Recipe.objects.filter(Q(Name__contains = searched) | Q(subcategory__type__contains = searched))
        return render(request, 'main/Search.html', {'searched': searched, 'results' : results})
    else:
        return render(request, 'main/Search.html', {})