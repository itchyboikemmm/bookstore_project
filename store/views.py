from django.shortcuts import render
from django.db.models import Count
from .models import Book, Category

def landing_page(request):
    books = Book.objects.all() # gather all books galing sa database
    best_sellers = Book.objects.filter(is_best_seller=True)[:8]
    categories = Category.objects.annotate(book_count=Count('book'))
    return render(request, 'store/landing_page.html', {'books': books,
                                                       'best_sellers': best_sellers,
                                                       'categories': categories,}) # sends it sa template
