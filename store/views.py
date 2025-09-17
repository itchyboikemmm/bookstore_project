from django.shortcuts import render
from .models import Book

def landing_page(request):
    books = Book.objects.all() # gather all books galing sa database
    return render(request, 'store/landing_page.html', {'books': books}) # sends it sa template