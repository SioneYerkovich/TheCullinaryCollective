from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe, Category, SubCategory, Review
from django import forms
from django.core.exceptions import ValidationError

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    last_name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control mb-3"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control mb-3'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    def clean_email(self):
        #From all of the submitted form data, retireve the email field data and store in the variable for checking
        email = self.cleaned_data.get('email')
        #Check if email already exists
        if User.objects.filter(email=email).exists():
            #if it exists, throw this error
            raise ValidationError("This email address is already in use. Please use a different email.")
        return email

class RecipeForm(forms.ModelForm):
    Name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={"class":"form-control mb-3"}), required=True)
    author = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={"class":"form-control mb-3"}), required=True)
    description = forms.CharField(max_length = 600, widget=forms.Textarea(attrs={"class":"form-control mb-3"}), required=True)
    ingredients = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control mb-3"}), required=True)
    instructions = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control mb-3"}), required=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={"class":"form-select mb-3"}), required=True)
    subcategory = forms.ModelChoiceField(queryset=SubCategory.objects.all(), widget=forms.Select(attrs={"class":"form-select mb-3"}) ,required=True)

    class Meta:
        model = Recipe
        fields = ['Name', 'author', 'image', 'description', 'ingredients', 'instructions', 'category', 'subcategory']

class ReviewForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control mb-3", "rows" : "6", "cols" : "6" }), required=True)

    class Meta:
        model = Review
        fields = ['content']