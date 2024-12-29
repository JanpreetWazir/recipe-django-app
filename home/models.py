from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(null=True , blank=True)


class Product(models.Model):
    name = models.CharField(max_length=10)
    price = models.FloatField()

class Car(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self)-> str:
        return self.price



# Create your models here.
