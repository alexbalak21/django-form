from django.db import models


class Author(models.Model):
    name = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(null=False, blank=False, max_length=255)
    author = models.ForeignKey('Author', null=False, blank=False,
                               on_delete=models.CASCADE, related_name='book_author')
