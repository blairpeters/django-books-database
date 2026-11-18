
from django.shortcuts import render, redirect
from core.my_forms import BookForm
from django.contrib import messages
from core.models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html',{"books":books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

    #     check validation
        if form.is_valid():
            form.save()# Create your views here.

            messages.success(request, 'Book successfully added!')
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add-book.html', {"form": form})
