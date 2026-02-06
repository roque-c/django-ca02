from django.shortcuts import render, redirect

# Create your views here.

from .forms import BookForm 
  

def add_book(request): 

    if request.method == "POST": 
        form = BookForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('add_book') 
    else: 
        form = BookForm() 
    return render(request, 'mforms_app/add_book.html', {'form': form}) 

'''
This view: 

    Displays the form (GET) 

    Saves data to the database (POST) 

''' 