from django.contrib import admin
from .models import Category, Author, Book

# register category
@admin.register(Category)
class CatergoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Author)
# register author
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
# register book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price', 'is_best_seller', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('is_best_seller', 'category', 'author')
    search_fields = ('title', 'author_name')