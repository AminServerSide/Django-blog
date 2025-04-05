from django import forms
from django.core.validators import ValidationError

from blog.models import Message


class ContactUsFromForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)
    text = forms.CharField(max_length=410 , label='Your message')


    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')

        if name == text:
            raise ValidationError("Your name and text can't be the same" , code="name_text_same")


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            "title" : forms.TextInput(attrs={'class':'form-control'}),
        }
