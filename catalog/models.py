from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
import uuid


class Genre(models.Model):
    name = models.CharField(max_length=255,unique=True,help_text="enter book genre")
    
    
    def __str__(self):
        return self.name
    
    
    
    
    def get_absolute_url(self):
        return reverse("genre_detail", args=[str(self.id)])
    
    
    class Meta:
        constraints=[
			UniqueConstraint(
				Lower('name'),
				name = 'genre_name_case_insensitive_unique',
				violation_error_message = "genre already exists"
			)
		]
		
	

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name= models.CharField(max_length=50)
    date_of_birth=models.DateField(null=True,blank=True)
    death = models.DateField(null=True,blank=True)
    
    
    def __str__(self):
        return f"{self.first_name}"
    
    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])
    
    

class Book(models.Model):
    title =models.CharField(max_length=255)
    language = models.CharField(max_length=255,default='English',null=True)
    author=models.ForeignKey(Author,on_delete=models.RESTRICT,null=True)
    summary = models.TextField(max_length=1083,help_text="Brief description of the book")
    isbn = models.CharField('ISBN',max_length=13,unique=True)
    genre = models.ManyToManyField(Genre,help_text="select a genre")
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail',args=[str(self.id)])
    
    


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    book = models.ForeignKey(Book,on_delete=models.RESTRICT,null=True)
    imprint = models.CharField(max_length=244)
    due_back = models.DateField(null=True,blank=True)
    
    LOAN_STATUS ={
		"M":'Maintance',
		"O":'On loan',
		"A":'Available'
	}
    
    status = models.CharField(max_length=2,choices=LOAN_STATUS,blank=True,default="M")
    
    class Meta:
        ordering = ['due_back']		
        
        
    def __str__(self):
        return f"{self.id}({self.book.title})"
    
    
    
    
    
	




	
	
    
    
    
    
