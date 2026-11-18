from django.db import models

# Create your models here.
GENRES = [
    ('Romance', 'Romance'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Thriller', 'Thriller'),
    ('Fantasy', 'Fantasy'),
    ('Horror', 'Horror'),
    ('Music', 'Music'),
]
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    isbn = models.IntegerField()
    description = models.TextField()
    genre = models.CharField(max_length=200, choices=GENRES)
    class Meta:
        db_table = 'book'
