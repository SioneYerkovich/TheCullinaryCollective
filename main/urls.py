from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

    
#These URL patterns will render a page using called funtions (defined in views.py). The "name" parameter act as shortcuts
urlpatterns = [
    path("", views.home_view, name="TCC-home"),
    path("daily-recipes/breakfast/", views.daily_recipes_breakfast_view, name="daily-recipes-breakfast"),
    path("daily-recipes/lunch/", views.daily_recipes_lunch_view, name="daily-recipes-lunch"),
    path("daily-recipes/dinner/", views.daily_recipes_dinner_view, name="daily-recipes-dinner"),
    path("daily-recipes/dessert/", views.daily_recipes_dessert_view, name="daily-recipes-dessert"),
    path("daily-recipes/drinks/", views.daily_recipes_drinks_view, name="daily-recipes-drinks"),
    path("Health-and-diet/vegetarian/", views.health_recipes_vegetarian_view, name="health-recipes-vegetarian"),
    path("Health-and-diet/keto/", views.health_recipes_keto_view, name="health-recipes-keto"),
    path("holidays/mothers-day/", views.holidays_md_view, name="holiday-recipes-MD"),
    path("holidays/new-years/", views.holidays_ny_view, name="holiday-recipes-NY"),
    path("like/breakfast/<recipe_id>/", views.like_view_breakfast, name="like-recipe-breakfast"),
    path("like/lunch/<recipe_id>/", views.like_view_lunch, name="like-recipe-lunch"),
    path("like/dinner/<recipe_id>/", views.like_view_dinner, name="like-recipe-dinner"),
    path("like/dessert/<recipe_id>/", views.like_view_dessert, name="like-recipe-dessert"),
    path("like/drinks/<recipe_id>/", views.like_view_drinks, name="like-recipe-drinks"),
    path("like/vegetarian/<recipe_id>/", views.like_view_vegetarian, name="like-recipe-vegetarian"),
    path("like/keto/<recipe_id>/", views.like_view_keto, name="like-recipe-keto"),
    path("like/MD/<recipe_id>/", views.like_view_md, name="like-recipe-md"),
    path("like/NY/<recipe_id>/", views.like_view_ny, name="like-recipe-ny"),
    path('favorite/breakfast/<recipe_id>/', views.toggle_favourite_breakfast, name='toggle-favourite-breakfast'),
    path('favorite/lunch/<recipe_id>/', views.toggle_favourite_lunch, name='toggle-favourite-lunch'),
    path('favorite/dinner/<recipe_id>/', views.toggle_favourite_dinner, name='toggle-favourite-dinner'),
    path('favorite/dessert/<recipe_id>/', views.toggle_favourite_dessert, name='toggle-favourite-dessert'),
    path('favorite/drinks/<recipe_id>/', views.toggle_favourite_drinks, name='toggle-favourite-drinks'),
    path('favorite/vegetarian/<recipe_id>/', views.toggle_favourite_vegetarian, name='toggle-favourite-vegetarian'),
    path('favorite/keto/<recipe_id>/', views.toggle_favourite_keto, name='toggle-favourite-keto'),
    path('favorite/MD/<recipe_id>/', views.toggle_favourite_md, name='toggle-favourite-md'),
    path('favorite/NY/<recipe_id>/', views.toggle_favourite_ny, name='toggle-favourite-ny'),
    path('favorite/recipe-book/<recipe_id>/', views.remove_favourite_recipebook, name='remove-favourite-recipebook'),
    path("review/breakfast/<recipe_id>/", views.review_breakfast_view, name="add-review-breakfast"),
    path("review/lunch/<recipe_id>/", views.review_lunch_view, name="add-review-lunch"),
    path("review/dinner/<recipe_id>/", views.review_dinner_view, name="add-review-dinner"),
    path("review/dessert/<recipe_id>/", views.review_dessert_view, name="add-review-dessert"),
    path("review/drinks/<recipe_id>/", views.review_drinks_view, name="add-review-drinks"),
    path("review/vegetarian/<recipe_id>/", views.review_vegetarian_view, name="add-review-vegetarian"),
    path("review/keto/<recipe_id>/", views.review_keto_view, name="add-review-keto"),
    path("review/MD/<recipe_id>/", views.review_md_view, name="add-review-md"),
    path("review/NY/<recipe_id>/", views.review_ny_view, name="add-review-ny"),
    path('review/edit/breakfast/<int:recipe_id>/<int:review_id>/', views.edit_review_breakfast_view, name="edit-review-breakfast"),
    path('review/edit/lunch/<int:recipe_id>/<int:review_id>/', views.edit_review_lunch_view, name="edit-review-lunch"),
    path('review/edit/dinner/<int:recipe_id>/<int:review_id>/', views.edit_review_dinner_view, name="edit-review-dinner"),
    path('review/edit/dessert/<int:recipe_id>/<int:review_id>/', views.edit_review_dessert_view, name="edit-review-dessert"),
    path('review/edit/drinks/<int:recipe_id>/<int:review_id>/', views.edit_review_drinks_view, name="edit-review-drinks"),
    path('review/edit/vegetarian/<int:recipe_id>/<int:review_id>/', views.edit_review_vegetarian_view, name="edit-review-vegetarian"),
    path('review/edit/keto/<int:recipe_id>/<int:review_id>/', views.edit_review_keto_view, name="edit-review-keto"),
    path('review/edit/MD/<int:recipe_id>/<int:review_id>/', views.edit_review_md_view, name="edit-review-md"),
    path('review/edit/NY/<int:recipe_id>/<int:review_id>/', views.edit_review_ny_view, name="edit-review-ny"),
    path('review/delete/breakfast/<int:recipe_id>/<int:review_id>/', views.delete_review_breakfast_view, name='delete-review-breakfast'),
    path('review/delete/lunch/<int:recipe_id>/<int:review_id>/', views.delete_review_lunch_view, name='delete-review-lunch'),
    path('review/delete/dinner/<int:recipe_id>/<int:review_id>/', views.delete_review_dinner_view, name='delete-review-dinner'),
    path('review/delete/dessert/<int:recipe_id>/<int:review_id>/', views.delete_review_dessert_view, name='delete-review-dessert'),
    path('review/delete/drinks/<int:recipe_id>/<int:review_id>/', views.delete_review_drinks_view, name='delete-review-drinks'),
    path('review/delete/vegetarian/<int:recipe_id>/<int:review_id>/', views.delete_review_vegetarian_view, name='delete-review-vegetarian'),
    path('review/delete/keto/<int:recipe_id>/<int:review_id>/', views.delete_review_keto_view, name='delete-review-keto'),
    path('review/delete/MD/<int:recipe_id>/<int:review_id>/', views.delete_review_md_view, name='delete-review-md'),
    path('review/delete/NY<int:recipe_id>/<int:review_id>/', views.delete_review_ny_view, name='delete-review-ny'),
    path("login/", views.login_view, name="TCC-login"),
    path("logout/", views.logout_user, name="TCC-logout"),
    path("login/register/", views.register_view, name="TCC-register"),
    path("recipe-book/", views.recipe_book_view, name="recipe-book"),
    path("recipe-book/edit/<recipe_id>/", views.edit_recipe_view, name="recipe-book-edit"),
    path("recipe-book/delete/<recipe_id>/", views.delete_recipe_view, name="recipe-book-delete"),
    path("search/", views.search_recipe_view, name="search-recipe"),


    #This portion is all working together, as the password reset section
    path("reset-password/", auth_views.PasswordResetView.as_view(template_name="main/PWForgot.html"), name="password_reset"),
    path("reset-password-sent/", auth_views.PasswordResetDoneView.as_view(template_name="main/PWResetSent.html"), name="password_reset_done"),
    path("reset-password-confirmation/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="main/PWResetConfirm.html"), name="password_reset_confirm"),
    path("reset-password-completed/", auth_views.PasswordResetCompleteView.as_view(template_name="main/PWResetComplete.html"), name="password_reset_complete"),

    
    #Order of events:
    #1 - Submit email form
    #2 - Email sent success message
    #3 - Link to password reset form in email
    #4 - Password successfully changed message
    
]