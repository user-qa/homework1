from django.shortcuts import render
from book.models import BookModel


# Create your views here.
def home_view(request):
    books = BookModel.objects.all()
    context = {
        'books_list':books
    }
    return render(request, 'home_view.html', context=context)