from django.contrib import admin
from .models import Author, Country, Genre, BookCopy, Book, Reader, Order, Librarian, CustomUser

from import_export import resources
from .models import Book
from import_export.admin import ImportExportModelAdmin

class BookResource(resources.ModelResource):
    class Meta:
        model = Book

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    pass

@admin.register(Reader)
class Reader(admin.ModelAdmin):
    pass

@admin.register(Order)
class Order(admin.ModelAdmin):
    pass

@admin.register(Librarian)
class Librarian(admin.ModelAdmin):
    pass
