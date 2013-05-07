from django.db import models


class MyModel(models.Model):
    myfield = models.CharField('myfield', max_length=3, choices = (['longer_than_3', 'longer_than_3')]
