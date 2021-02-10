from django import forms
from mainapp import models

class login(forms.Form):
    username=forms.CharField(max_length=15)
    password=forms.CharField(widget=forms.PasswordInput)

class signup(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=models.writer
        fields='__all__'
        widgets = {
        		'slug': forms.HiddenInput(),
        }