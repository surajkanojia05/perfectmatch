from django import forms
from django.forms import widgets
from .models import partner
from django.forms import ModelForm

class addprofileform(ModelForm):
    class Meta:
        model = partner
        fields = ('name', 'cast', 'religion', 'age', 'description', 'tag', 'gender', 'qualifications', 'occupation', 'height', 'image1', 'image2', 'image3')

        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'cast':forms.TextInput(attrs={'class': 'form-control'}),
            'religion':forms.TextInput(attrs={'class': 'form-control'}),
            'age':forms.NumberInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
            'tag':forms.TextInput(attrs={'class': 'form-control'}),
            'gender':forms.TextInput(attrs={'class': 'form-control'}),
            'qualifications':forms.TextInput(attrs={'class': 'form-control'}),
            'occupation':forms.TextInput(attrs={'class': 'form-control'}),
            'height':forms.TextInput(attrs={'class': 'form-control'}),
            'image1':forms.FileInput(attrs={'class': 'form-control'}),
            'image2':forms.FileInput(attrs={'class': 'form-control'}),
            'image3':forms.FileInput(attrs={'class': 'form-control'}),
        }