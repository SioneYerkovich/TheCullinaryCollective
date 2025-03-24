from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe, Category, SubCategory
from django import forms

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

class RecipeForm(forms.ModelForm):
    Name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={"class":"form-control mb-3"}))
    ingredients = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control mb-3"}))
    instructions = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control mb-3"}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={"class":"form-select mb-3"}), required=True)
    subcategory = forms.ModelChoiceField(queryset=SubCategory.objects.all(), widget=forms.Select(attrs={"class":"form-select mb-3"}) ,required=True)

    class Meta:
        model = Recipe
        fields = ['Name', 'image', 'ingredients', 'instructions', 'category', 'subcategory']