from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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