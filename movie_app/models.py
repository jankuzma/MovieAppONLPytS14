from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=123)
    last_name = models.CharField(max_length=123)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField(max_length=123)
    city = models.CharField(max_length=123)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.city}"


class Movie(models.Model):
    title = models.CharField(max_length=123)
    year = models.IntegerField()
    director = models.ForeignKey(Person, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title



