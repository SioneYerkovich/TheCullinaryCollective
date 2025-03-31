from django.contrib import admin
from .models import Recipe, Category, SubCategory, Review, Favourite

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Review)
admin.site.register(Favourite)