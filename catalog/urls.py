from django.urls import path
from . import views


urlpatterns = [
	
	path('about/',views.about, name='about'),
	path('',views.index, name='index'),
	path('books/',views.BookListView.as_view(), name='books'),
	path('book/<int:pk>',views.BookDetailView.as_view(), name='book-detail'),
	path('author/<int:pk>',views.AuthorDetailView.as_view(), name='author-detail'),
	path('authors/',views.Author_ListView, name='authors'),
	
]

