from django.contrib import admin
from .models import Book

# Register the Book model so it shows up in the admin dashboard
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')
