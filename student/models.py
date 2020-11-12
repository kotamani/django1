from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=10)
    age = models.IntegerField()
    per = models.FloatField()

    def __str__(self):
        return self.name
