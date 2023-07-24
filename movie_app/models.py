from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=123)
    last_name = models.CharField(max_length=123)
    year = models.IntegerField()


class Genre(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name
