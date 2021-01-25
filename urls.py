"""personal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from personal.views import hello, info, get_numbers, bio, books, get_authors, CountryView, HomePage, BookTable

from rest_framework.routers import SimpleRouter

from personal.views import BookViewSet, BookCopyViewSet, CountryViewSet, AuthorViewSet, ReaderViewSet, OrderViewSet

router = SimpleRouter()
router.register('countries-new', CountryViewSet)
router.register('books-new', BookViewSet)
router.register('books-copy-new', BookCopyViewSet)
router.register('author-new', AuthorViewSet)
router.register('reader-new', ReaderViewSet)
router.register('order-new', OrderViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', info),

    path('numbers/', get_numbers),
    path('test-template/', bio),
    path('home-page/', books),
    path('get-authors/', get_authors),
    path('countries/', CountryView.as_view()),
    path('home/', HomePage.as_view(template_name="home.html")),
    path('bookinfo/', BookTable.as_view()),
] + router.urls
