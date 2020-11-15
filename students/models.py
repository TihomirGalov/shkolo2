from django.contrib.postgres.fields import ArrayField
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    marks = ArrayField(models.IntegerField(), null=True, blank=True)
    black_marks = ArrayField(models.TextField(), null=True, blank=True)
    absences = ArrayField(models.DateField(), null=True, blank=True)
