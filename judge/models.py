from tkinter import CASCADE
from django.db import models
from django.forms import CharField

# Create your models here.

class Problem(models.Model):
    name = models.CharField(max_length=200)
    problem_statement = models.CharField(max_length=500)
    # code = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Solution(models.Model):
    problem = models.ForeignKey(Problem , on_delete=models.CASCADE)
    verdict = models.CharField(max_length=50)
    submitted_at = models.DateTimeField()
    submitted_code = models.CharField(max_length=255)

    def __str__(self):
        return self.verdict

class Testcases(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input = models.CharField(max_length=255)
    output = models.CharField(max_length=255)

    def __str__(self):
        return self.input

