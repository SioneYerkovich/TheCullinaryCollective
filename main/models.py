from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

#Recipe model
class Recipe(models.Model):
    #user who adds the recipe
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')

    #details of the recipe
    Name = models.CharField(max_length=100)
    image = CloudinaryField('image')#image = models.ImageField(upload_to='recipes/')
    author = models.TextField(max_length=50)
    description = models.TextField(max_length=600)
    ingredients = models.TextField()
    instructions = models.TextField()
    likes = models.ManyToManyField(User, related_name='likes')

    #connections to the category hierarchy
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('SubCategory', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Name
    
#Category model
#These can only be added and modified using django admin panel (navigate using domain url + /admin)
class Category(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

#SubCategory model
#these can only be added and modified using django admin panel (navigate using domain url + /admin)
class SubCategory(models.Model):
    type = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.type

#Review model
class Review(models.Model):
    #user who creates a review
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    #recipe they are reviewing
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='reviews') 
    #review body content and timestamp (auto captured)
    content = models.TextField(max_length=200) 
    timestamp = models.DateTimeField(auto_now_add=True)

    #ensures users can only create one review per recipe
    class Meta:
        unique_together = ('user', 'recipe')

    def __str__(self):
        return f"Review by {self.user.username} for {self.recipe.Name}"
    
#Favourite model
class Favourite(models.Model):
    #user who adds a favourite
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    #recipe they are favouriting
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favourited_by')

    def __str__(self):
        return f"{self.user.username} favourited {self.recipe.Name}"