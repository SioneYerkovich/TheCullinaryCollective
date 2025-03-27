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