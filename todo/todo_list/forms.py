from django import forms
from .models import List,User
class ListForm(forms.ModelForm):
    class Meta:
        model=List
        fields=['item','completed']
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['email','password']
class CreateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=[
            'email',
            'password',
            'name',
            'desg'
        ]


