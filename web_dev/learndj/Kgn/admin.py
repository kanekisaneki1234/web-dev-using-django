from django.contrib import admin

# Register your models here.
from .models import Kgn, book, author

admin.site.register(Kgn)
admin.site.register(book)
admin.site.register(author)
