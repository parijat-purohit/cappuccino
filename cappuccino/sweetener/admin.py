from django.contrib import admin
from sweetener.models import Book, Author

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    search_fields = ['name']
    raw_id_fields = ['author']


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
