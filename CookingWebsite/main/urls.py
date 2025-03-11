from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="TCC-home"),
    path("daily-recipes/", views.daily_recipes_view, name="TCC-daily-recipes"),
    path("holidays/", views.holidays_view, name="TCC-holidays"),

]