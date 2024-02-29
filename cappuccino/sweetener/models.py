from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"Author: {self.name}"


class Book(models.Model):
    name = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Book: {self.name}, Author: {self.author}"
