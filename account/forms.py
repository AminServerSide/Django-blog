from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'input100'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input100'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError("Username or password is incorrect", code="invalid_login")

        return cleaned_data




class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name')

