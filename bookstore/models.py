from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return f'{self.title}'

class CommentBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                                    related_name='book_comment')
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)