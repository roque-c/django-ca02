from django.shortcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)

        # ✅ Django automatically runs our clean_*() methods here
        # If ANY field fails validation, is_valid() returns False
        # and the form is returned with errors attached to each field
        if form.is_valid():
            form.save()
            return redirect('add_book')

        # If form is NOT valid, we fall through to render below
        # The form object now carries all the error messages

    else:
        # GET request — show a blank form
        form = BookForm()

    # Render the template, passing the form (with or without errors)
    return render(request, 'mforms_app/add_book.html', {'form': form})
