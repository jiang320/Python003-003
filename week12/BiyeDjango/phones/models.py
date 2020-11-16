from django.db import models

# Create your models here.


class Phones(models.Model):
    name= models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    comment=models.CharField(max_length=1000)
    stmscore=models.FloatField()

    class Meta:
        managed=False
        db_table= 'phones'
