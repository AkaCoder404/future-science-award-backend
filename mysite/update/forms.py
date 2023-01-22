from django import forms
from django.forms import ClearableFileInput

from .models import MyUser, MyUserUploads

class UploadFile(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('name','affiliation', 'email', 'category', 'contribution', 'research',)

class UploadForm(forms.ModelForm):
    class Meta:
        model = MyUserUploads
        fields = ('file', )
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }