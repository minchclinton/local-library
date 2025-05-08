from django.contrib import admin
from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','summary','isbn',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth','death')
class GenreAdmin(admin.ModelAdmin):
    pass
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter=('status','due_back')
    list_display = ('id','imprint','due_back')

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(BookInstance,BookInstanceAdmin)

