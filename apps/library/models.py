from django.db import models
from apps.authentication.models import Student
import datetime
from django.utils import timezone
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=350)
    description = models.CharField(max_length=450)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=350)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/library/booksCover")
    category = models.CharField(max_length=220)
    pdf = models.FileField(upload_to="images/library/boks")

    def __str__(self):
        return self.name


class downloaded(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student} {" downlaoded "} {self.book}'
