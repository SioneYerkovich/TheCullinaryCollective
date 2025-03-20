from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipeName = models.CharField(max_length=100)
    image = models.ImageField()
    author = models.CharField(max_length=50)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)