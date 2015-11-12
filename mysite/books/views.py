from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context
from books.models import *


def Home(request):
    return render_to_response("home.html")

def AddAuthorpage(request):
    return render_to_response("author.html")
    
def AddAuthor(request):
    post = request.POST
    newauthor = Author(
        AuthorID = post['authorid'],
        Name = post['name'],
        Age = post['age'],
        Country = post['country'],
    )
    newauthor.save()
    return HttpResponseRedirect("/home/")

def AddBookpage(request):
    c = Context({'ID':request.GET['ID']})
    return render_to_response("book.html", c)
    
def AddBook(request):
    post = request.POST
    auth = Author.objects.get(AuthorID = post['AuthorID'])
    newbook = Book(
        AuthorID = auth,
        ISBN = post['ISBN'],
        Title = post['Title'],
        Publisher = post['Publisher'],
        Publishdate = post['Publishdate'],
        Price = post['Price'],
    )
    newbook.save()
    return HttpResponseRedirect("/home/")
    
def SearchAuthor(request):
    if request.POST:
        author_list = Author.objects.filter(Name=request.POST['authorstring'])
        c = Context({'author_list':author_list})
        return render_to_response("authors.html", c)
        
def SearchBook(request):
    authorid = request.GET['ID']
    auth = Author.objects.get(AuthorID = authorid)
    book_list = Book.objects.filter(AuthorID = auth)
    c = Context({'book_list':book_list})
    d = Context({'authorid':authorid})
    return render_to_response("books.html", c, d)
    
def Delete(request):
    bookid = request.GET['ID']
    Book.objects.get(ISBN = bookid).delete()
    return HttpResponseRedirect("/home/")
    
def Information(request):
    bookid = request.GET['ID']
    Infor = Book.objects.get(ISBN = bookid)
    c = Context({'Infor':Infor})
    return render_to_response("information.html", c)

    
    