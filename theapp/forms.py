from django import forms
from django.forms import widgets
from .models import partner
from django.forms import ModelForm

class addprofileform(ModelForm):
    class Meta:
        model = partner
        fields = ('name', 'father_name', 'mother_name', 'address', 'cast', 'religion', 'age', 'description', 'tag', 'gender', 'qualifications', 'occupation', 'height', 'image1', 'image2', 'image3')
        
        labels = {
            'name': 'Enter your name:',
            'father_name': "Enter your Father's name:",
            'mother_name': "Enter your Mother's name:",
            'address': 'Enter your location and city:',
            'cast': 'Enter your cast:',
            'religion': 'Enter your religion:',
            'age': 'Enter your Age:',
            'description': 'Explain about yourself:',
            'gender': 'Enter Gender:',
            'qualifications': 'Enter your qualifications:',
            'occupation': 'Enter your Occupation:',
            'height': 'Enter your height in feets:',
            'image1': 'Enter image here:',
            'image2': 'Enter image here:',
            'image3': 'Enter image here:',
        }
        
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'father_name':forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name':forms.TextInput(attrs={'class': 'form-control'}),
            'address':forms.TextInput(attrs={'class': 'form-control'}),
            'cast':forms.TextInput(attrs={'class': 'form-control'}),
            'religion':forms.TextInput(attrs={'class': 'form-control'}),
            'age':forms.NumberInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control'}),
            'gender':forms.TextInput(attrs={'class': 'form-control'}),
            'qualifications':forms.TextInput(attrs={'class': 'form-control'}),
            'occupation':forms.TextInput(attrs={'class': 'form-control'}),
            'height':forms.TextInput(attrs={'class': 'form-control'}),
            'image1':forms.FileInput(attrs={'class': 'form-control'}),
            'image2':forms.FileInput(attrs={'class': 'form-control'}),
            'image3':forms.FileInput(attrs={'class': 'form-control'}),
        }
