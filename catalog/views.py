from django.shortcuts import render
from .models import *


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