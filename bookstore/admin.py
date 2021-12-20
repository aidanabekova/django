from django.contrib import admin
from bookstore import models

admin.site.register(models.Book)
admin.site.register(models.CommentBook)