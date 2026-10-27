import traceback
from collections import namedtuple

from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.shortcuts import redirect


from .models import Book, Customer
from .forms import BookForm

# Create your views here.
def index(request):
    context = {'app_name': 'store'}
    return render(request, 'store/index.html', context)

def booklist(request):
    queryset = Book.objects.all() #SELECT * FROM book;
    qyertset = Book.objects.filter(id=1)  #array
    context = {'books': queryset}
    return render(request, 'store/booklist.html', context)

def bookview(request, id):
    book = Book.objects.get(id=id) #single, 여러개 있으면 Multi object exception
    context = {'book': book}
    return render(request, 'store/bookview.html', context)

def postbook(request):
    context = {}
    if request.method == 'POST':
        result = False
        try:
            bookname = request.POST.get('bookname', '')
            publisher = request.POST.get('publisher', '')
            price = request.POST.get('price')
            book = Book(bookname=bookname, publisher=publisher, price=price)
            book.save()
            result = True
        except:
            result = False
        context = {'result': result}
        return render(request, 'store/postresult.html', context)

    return render(request, 'store/postbook.html', context)


def createbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  #INSERT INTO book
            return redirect('booklist')
    form = BookForm()
    return render(request, 'store/createbook.html', {'form': form})

def editbook(request, id):
    if request.method == 'POST':
        result = '실패'
        book = Book.objects.get(id=id)
        form = BookForm(request.POST, instance=book)
        try:
            if form.is_valid():
                form.save()
                result = '성공'
            else:
                result = form.errors
        except:
            result = traceback.format_exc()
        context = {'result': result}
        return render(request, 'store/postresult.html', context)
    else:  #method GET
        book = Book.objects.get(id=id)
        form = BookForm(instance=book)
        return render(request, 'store/editbook.html', {'form': form})

def deletebook(request, id):
    #성공하면 '성공' 실패하면 '실패' 라고 적히도록 수정
    if request.method == 'POST':
        result = '실패'
        try:
            book = Book.objects.get(id=id)
            book.delete()
            result = '성공'
        except:
            pass
            #result = traceback.format_exc()
        context = {'result': result}
        return render(request, 'store/postresult.html', context)
    else:
        book = Book.objects.get(id=id)
        return render(request, 'store/deletebook.html', {'book': book})

