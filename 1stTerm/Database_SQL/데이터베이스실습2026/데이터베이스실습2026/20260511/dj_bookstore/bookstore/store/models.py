from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    bookname = models.CharField(max_length=40, null=True)
    publisher = models.CharField(max_length=40, null=True)
    price = models.IntegerField(null=True)

    class Meta:
        db_table='book'

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=True, verbose_name='이름')
    address = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'customer'
