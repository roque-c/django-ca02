from django import forms
from .models import Book


class BookForm(forms.ModelForm): 

    class Meta: 

        model = Book 

#hey 11th grade, here Django automatically creates the form fields based on the model. 
        fields = ['title', 'author', 'published_year'] 
 