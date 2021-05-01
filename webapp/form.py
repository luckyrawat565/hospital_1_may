from django.forms import ModelForm
from django import forms
from .models import User

class user_signup(ModelForm):
    password1 = forms.CharField(label = 'pasword',widget = forms.PasswordInput())
    password2 = forms.CharField(label = 'conform pasword',widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ['user_name','first_name','last_name']


    def clean(self):
        cleaned_data = super().clean()
        valpwd = self.cleaned_data['password1']
        valrpwd = self.cleaned_data['password2']
        if valpwd != valrpwd:
            raise forms.ValidationError('password does not match')