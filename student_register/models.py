from django.db import models
from datetime import datetime, time

SEX_CHOICES = [
    ('Garçon', 'Garcon'),
    ('Fille', 'Fille'),
]

class Level(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    birthday = models.DateField("birthday Date(mm/dd/yy)", auto_now_add= False, auto_now=False, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,  blank = True)





