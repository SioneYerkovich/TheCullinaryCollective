from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="TCC-home"),
    path("daily-recipes/breakfast/", views.daily_recipes_breakfast_view, name="daily-recipes-breakfast"),
    path("daily-recipes/lunch/", views.daily_recipes_lunch_view, name="daily-recipes-lunch"),
    path("holidays/", views.holidays_view, name="TCC-holidays"),

]