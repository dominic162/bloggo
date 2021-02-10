from django import forms
from mainapp import models

class addblog(forms.ModelForm):

    class Meta:
        model=models.blog
        fields='__all__'
        widgets = {
        			'slug': forms.HiddenInput(),
        			'written_by': forms.HiddenInput(),
        			}

class contact(forms.ModelForm):

    class Meta:
        model=models.contact
        fields='__all__'
        widgets={
            'sno':forms.HiddenInput(),
        }