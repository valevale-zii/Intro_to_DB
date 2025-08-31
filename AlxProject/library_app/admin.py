from django.contrib import admin
from .models import Book, Member, Borrow

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'joined_date')


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('member', 'book', 'borrow_date', 'return_date', 'is_returned')
    actions = ['mark_as_returned']

    def mark_as_returned(self, request, queryset):
        for borrow in queryset:
            if not borrow.is_returned():
                borrow.return_book()
        self.message_user(request, "Selected books have been marked as returned.")

    mark_as_returned.short_description = "Mark selected borrowed books as returned"
