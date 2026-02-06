from django.db import models

# Create your models here.
# heyya 11th grade, this model represents the data we want to store in the database. 
class Book(models.Model): 
    title = models.CharField(max_length=100) 
    author = models.CharField(max_length=100) 
    published_year = models.IntegerField() 

    def __str__(self): 
        return self.title 
 