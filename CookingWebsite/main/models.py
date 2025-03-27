from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Recipe model
class Recipe(models.Model):
    #user who adds the recipe
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')

    #details of the recipe
    Name = models.CharField(max_length=100)
    image = models.ImageField()
    author = models.TextField(max_length=50)
    description = models.TextField(max_length=600)
    ingredients = models.TextField()
    instructions = models.TextField()

    #connections to the category hierarchy
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('SubCategory', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Name
    
#Category model
class Category(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

#SubCategory model
class SubCategory(models.Model):
    type = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.type