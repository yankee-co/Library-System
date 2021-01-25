from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Country, Book, Author, Reader, Order, BookCopy, Librarian

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']

class BookSerializer(ModelSerializer):

    authors = AuthorSerializer(many = True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'year_issued', 'authors']

class BookNestedSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['name']

class BookCopySerializer(ModelSerializer):

    book = BookNestedSerializer()

    class Meta:
        model = BookCopy
        # fields = '__all__'
        fields = ['id', 'order_number', 'book']

class ReaderSerializer(ModelSerializer):

    full_name = SerializerMethodField()

    def get_full_name(self, obj: Author) -> str:
        return obj.name + " " + obj.last_name

    class Meta:
        model = Reader
        fields = ['name', 'last_name' ,'full_name']



class LibrarianSerializer(ModelSerializer):
    class Meta:
        model = Librarian
        fields = ['first_name', 'last_name']

class OrderSerializer(ModelSerializer):

    bookcopy = BookCopySerializer()
    reader = ReaderSerializer()
    given_by = LibrarianSerializer()

    class Meta:
        model = Order
        fields = ['bookcopy', 'reader', 'given_by', 'taken_at', 'returned_at']

"""
class AuthorSerializer(ModelSerializer):

    full_name = SerializerMethodField()

    def get_full_name(self, obj: Author) -> str:
        return obj.first_name + " " + obj.last_name

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'country', 'full_name']
"""
