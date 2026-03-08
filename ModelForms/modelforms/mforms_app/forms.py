from django import forms
from .models import Book
import datetime

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year']

    # ✅ STUDENT TASK: Add custom validation for each field below

    def clean_title(self):
        title = self.cleaned_data.get('title')

        # Require the field to not be blank/whitespace only
        if not title or not title.strip():
            raise forms.ValidationError("Title is required and cannot be blank.")

        # Minimum length check
        if len(title.strip()) < 2:
            raise forms.ValidationError("Title must be at least 2 characters long.")

        return title.strip()

    def clean_author(self):
        author = self.cleaned_data.get('author')

        if not author or not author.strip():
            raise forms.ValidationError("Author name is required.")

        # Author name should only contain letters and spaces
        if not all(c.isalpha() or c.isspace() for c in author):
            raise forms.ValidationError("Author name should only contain letters and spaces.")

        return author.strip()

    def clean_published_year(self):
        year = self.cleaned_data.get('published_year')

        if year is None:
            raise forms.ValidationError("Published year is required.")

        current_year = datetime.datetime.now().year

        # Year must be realistic
        if year < 1000:
            raise forms.ValidationError("Please enter a valid 4-digit year (e.g. 1998).")

        if year > current_year:
            raise forms.ValidationError(f"Published year cannot be in the future. Max allowed: {current_year}.")

        return year
