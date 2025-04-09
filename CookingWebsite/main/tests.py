from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, Review

class UserCreationTest(TestCase):
    def test_create_user(self):
        #Create a user using this field data
        user = User.objects.create_user(
            username="testuser",
            password="password"
        )
        #Validate the test data
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("password"))

class RecipeCreationTest(TestCase):
    def test_create_recipe(self):
        #Create a user for the create recipe function and log in
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        #Create a recipe using this field data
        recipe = Recipe.objects.create(
            user=self.user,
            Name="test recipe",
            author="test author",
            description="test description",
            ingredients="test ingredients",
            instructions="prepare the test"
        )
        #Validate the test data
        self.assertEqual(recipe.Name, "test recipe")
        self.assertEqual(recipe.author, "test author")
        self.assertEqual(recipe.description, "test description")
        self.assertEqual(recipe.ingredients, "test ingredients")
        self.assertEqual(recipe.instructions, "prepare the test")
        self.assertEqual(recipe.user, self.user)


class ReviewCreationTest(TestCase):
    def test_create_review(self):
        #Create a user for the review and log in
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        #Create a recipe for the review using this field data
        FakeRecipe = Recipe.objects.create(
            user=self.user,
            Name="test recipe",
            author="test author",
            description="test description",
            ingredients="test ingredients",
            instructions="prepare the test"
        )
        #Create the review
        review = Review.objects.create(
            user=self.user,
            recipe=FakeRecipe,
            content="This is a test review"
        )
        #Validate the test data
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.recipe, FakeRecipe)
        self.assertEqual(review.content, "This is a test review")