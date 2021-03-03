from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from collections import Counter
import datetime
import json

from rest_framework.viewsets import ModelViewSet

from .models import Country, Author, Book, Reader, Order, BookCopy
from .serializers import CountrySerializer, BookSerializer, AuthorSerializer, ReaderSerializer, OrderSerializer, BookCopySerializer

def hello(request):
    return HttpResponse('OK')

def info(request):
    return HttpResponse(f'Now is: {datetime.datetime.now()}')

def get_numbers(request):

    values_list = [{'value':value, 'square':value**2} for value in range(20)]

    print(values_list)

    return render(
        request = request,
        template_name = 'numbers.html',
        context={
            'values_list' : values_list
        }
    )
def bio(request):


    return render(
        request = request,
        template_name = 'htmlbio.html',
        context={}
    )

def books(request):

    return render(
        request = request,
        template_name = 'books.html',
        context={
        'programming_name':'Язык программирования Python'
        }
    )

def get_authors(request):
    queryset = Author.objects.all()
    data = {'authors': queryset}
    return render(request, 'authors.html', context=data)

class CountryView(View):
    def get(self, *args, **kwargs):

        countries = Country.objects.all()

        data = []
        for c in countries:
            data.append({
                'name': c.name,
                'id': c.id
            })

        return JsonResponse(data, safe = False)


#ViewSets

class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCopyViewSet(ModelViewSet):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer

class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class HomePage(TemplateView):

    def get(self, *args, **kwargs):

        readers = Reader.objects.all()
        authors_list = Author.objects.all()
        books = Book.objects.all()

        def topFiveAuthors():
            authorTop = {}
            authCounter = Counter()
            counter = 0
            authors_full_names = []

            for book in books:
                authors = book.authors.all()

                for author in authors:
                    full_name = author.first_name + ' ' + author.last_name
                    authors_full_names.append(full_name)

            authors_full_names.sort()

            for full_name in authors_full_names:
                authCounter[full_name] += 1

            for key, value in sorted(dict(authCounter).items(), key = lambda kv: kv[1], reverse=True):
                counter += 1
                authorTop.update({key:value})
                if counter == 5: break

            return authorTop.items()

        def topLessBookInstances():
            ordersCounter = Counter()
            recreatedOrdersCounter = {}
            counter = 0

            for order in Order.objects.all():
                ordersCounter[order.bookcopy.book.name] += 1

            for key, value in sorted(dict(ordersCounter).items(), key = lambda kv: kv[1]):
                counter += 1
                recreatedOrdersCounter.update({key:value})
                if counter == 10: break
            return recreatedOrdersCounter.items()

        recreatedOrdersCounter = topLessBookInstances()

        authorTop = topFiveAuthors()


        return render(
            request = self.request,
            template_name = 'home.html',
            context={
            'readers' : readers,
            'authors_list' : authors_list,
            'books' : books,
            'authorTop': authorTop,
            'recreatedOrdersCounter' : recreatedOrdersCounter,
            }
            )

class BookTable(TemplateView):

    def get(self, *args, **kwargs):

        books = Book.objects.all()

        book_info_list = []

        how_many_books = 2

        for book in books:

            book_title = book.name
            authors = [f'{author.first_name} {author.last_name}' for author in book.authors.all()]
            year = book.year_issued
            genres = [genre.name for genre in book.genres.all()]

            orders_stat = {
                'processing': 0,
                'finished': 0,
            }

            for order in Order.objects.filter(bookcopy__book__name = book.name):
                if order.returned_at is None:
                    orders_stat['processing'] += 1
                    continue
                orders_stat['finished'] += 1




            booktr = {
                'book_title': book_title,
                'authors' : authors,
                'year': year,
                'genres': genres,
                'orders_stat': orders_stat
            }
            book_info_list.append(booktr)

            how_many_books -= 1
            if how_many_books == 0: break

        return render(
        request = self.request,
        template_name = 'bookinfo.html',
        context = {
            'book_info_list': book_info_list,
        }
        )
