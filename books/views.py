from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Books, HelpfulResources

# Create your views here.



def index(request):

    book = Books.objects.filter().order_by('book')

    context = {
        'book': book,
    }
    return render(request, 'books/already_read.html', context)

def going_read(request):

    book = Books.objects.filter().order_by('book')

    context = {
        'book': book,
    }
    return render(request, 'books/going-to-read.html', context)

def authors(request):

    auth_book = Books.objects.order_by('author_book').values('author_book').distinct()

    context = {
        'book': auth_book,

    }
    return render(request, 'books/authors.html', context)

def categories(request):

    book = Books.objects.filter().order_by('cat').values('cat').distinct()

    context = {
        'book': book,
    }
    return render(request, 'books/categories.html', context)

def subcategories(request):

    book = Books.objects.filter().order_by('sub_cat').values('sub_cat').distinct()

    context = {
        'book': book,
    }
    return render(request, 'books/subcategories.html', context)

def helpful_resources(request):

    link = HelpfulResources.objects.filter().order_by('description')

    context = {
        'link': link,
    }
    return render(request, 'books/helpful_resources.html', context)
