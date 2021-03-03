from django.db import models
from django.contrib.auth.models import AbstractUser

class Country(models.Model):

    name = models.CharField(max_length = 50, unique = True)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return f'{self.name}'

class Author(models.Model):

    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    country = models.ForeignKey('Country', on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.country})'

class Book(models.Model):

    name = models.CharField(max_length = 50)
    year_issued = models.PositiveSmallIntegerField()
    authors = models.ManyToManyField("Author")
    pages_count = models.PositiveSmallIntegerField()
    genres = models.ManyToManyField("Genre")

    def __str__(self):

        # Show authors
        queryset = self.authors.all()
        queryset_genres = self.genres.all()

        authors_list = []
        genres_list = []

        for author in queryset:
            authors_list.append(str(author))

        for genre in queryset_genres:
            genres_list.append(str(genre))

        authors_str = ', '.join(authors_list)
        genres_str = ', '.join(genres_list)

        return f'{self.name} by {authors_str} - {genres_str}'

class Genre(models.Model):

    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class BookCopy(models.Model):

    book = models.ForeignKey('Book', on_delete = models.CASCADE)
    order_number = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Book copies'

    def __str__(self):
        return f'{self.book.name} COPY / {self.order_number}'

class Reader(models.Model):
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.name} {self.last_name}"

"""
Order (books actually taken):
        - id (PK)
        - bookcopy (FK -> BookCopy)
        - reader (FK -> Reader)
        - taken_at (datetime)
        - returned_at (datetime)
        - given_by (FK -> Librarian)

 Librarian:
        - id (PK)
        - first_name
        - last_name
        - phone
        - employeed_date
        - unemployeed_date
"""

class Librarian(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone = models.IntegerField()
    employeed_date = models.DateTimeField()
    unemployeed_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#+380688553284

class Order(models.Model):
    bookcopy = models.ForeignKey('BookCopy', on_delete = models.CASCADE)
    reader = models.ForeignKey('Reader', on_delete = models.CASCADE)
    given_by = models.ForeignKey('Librarian', on_delete = models.CASCADE)
    taken_at = models.DateTimeField(null = True, blank = True)
    returned_at = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return f"{self.id} / {self.bookcopy} / {self.reader} / {self.given_by} / {self.taken_at} / {self.returned_at}"

class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=50, null=True, blank=True)
