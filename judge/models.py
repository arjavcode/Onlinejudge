from django.db import models

# Create your models here.

class Problem(models.Model):
    name = models.CharField(max_length=200)
    problem_statement = models.CharField(max_length=500)
    # code = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=200)

    def __str__(self):
        return self.name

