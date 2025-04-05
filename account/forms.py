from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}))


    def clean_username(self):
        user = authenticate(username=self.cleaned_data.get('username') , password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        raise ValidationError("username or password is wrong" , code="invalid_info")