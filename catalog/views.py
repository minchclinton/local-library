from django.shortcuts import render
from .models import *
from django.views import generic
from django.http import Http404

def index(request):
    number_of_books = Book.objects.all().count()
    number_of_authors = Author.objects.count()
    number_instances_available = BookInstance.objects.filter(status__exact='A').count()
    number_instances= BookInstance.objects.all().count()
    # Increment the number of visits in the session	
    if 'number_of_visits' in request.session:
        request.session['number_of_visits'] += 1
    else:
        request.session['number_of_visits'] = 1
	# Get the number of visits from the session
 
 
    number_of_visits = request.session['number_of_visits']
	



    context = {
		'number_of_books': number_of_books,
		'number_of_authors': number_of_authors,
		'number_instances_available': number_instances_available,
		'number_of_visits': number_of_visits,
		'number_instances': number_instances,
	}
    return render(request, 'catalog/index.html',context=context)





def about(request):
    return render(request, 'catalog/about.html')




class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/book_list.html'  # Specify your own template name
    context_object_name = 'book_list'  # Specify your own context object name
    paginate_by = 10  # Show 10 books per page

    def get_queryset(self):
        return Book.objects.all()[:5]  # Return the last five books added
    
    
    
    
    

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'  # Specify your own template name
    context_object_name = 'book'  # Specify your own context object name

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj is None:
            raise Http404("Book not found")
        return obj
    
   
class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'catalog/author_detail.html'  # Specify your own template name
    context_object_name = 'author'  # Specify your own context object name

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj is None:
            raise Http404("Author not found")
        return obj

def Author_ListView(request):
    author= Author.objects.all()
    context = {
        'author': author,
    }
    return render(request, 'catalog/author_list.html', context=context)


    