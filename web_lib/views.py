import re
from django.shortcuts import render, redirect
from web_lib.models import Author, Book

from.forms import SearchAuthor, PostAuthors, BookForm
from django.forms import modelform_factory

def main(request):

    book_form = BookForm()
    return render(request, "web_lib/main.html", {"form": book_form})


    #form = SearchAuthor(request.GET)
    #form_post = PostAuthors(request.POST)
    #return render(request, 'web_lib/main.html',{"form": form, "form_post": form_post})

def create_book(req):
    book_form = BookForm()
    if req.method == "POST":
        book_form = BookForm(req.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('books')
    return render(req, "web_lib/book_form.html", {"form": book_form})


def authors(request):
    if "author_uuid" in request.GET:
        return redirect('author_id', request.GET["author_uuid"])
    if request.method == "POST":
        data = dict()
        data["name"] = request.POST.get('name')
        data["age"] = request.POST.get('age')
        data["email"] = request.POST.get('email')
        Author.objects.create(**data)

    all_authors = {'authors': Author.objects.all()}
    return render(request, 'web_lib/authors.html', all_authors )

def author_id(request, pk):
    author = Author.objects.get(pk=pk)
    books_amount = author.book_set.count()
    found_author = {'author': author, 'books_amount': books_amount}
    return render(request, 'web_lib/author_id.html', found_author)

def books(request):
    all_books = {'books': Book.objects.all()}
    return render(request, 'web_lib/books.html', all_books)

def about(request):
    return render(request, 'web_lib/about.html')
