from django.db import models

# Create your models here.
class Product(models.Model):
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=200)
    price=models.IntegerField()
    pdescription=models.CharField(max_length=200)

    def __str__(self) :
        return self.pname