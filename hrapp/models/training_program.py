from django.db import models
from django.urls import reverse



class TrainingProgram(models.Model):

    title = models.CharField(max_length=55)
    start_date = models.DateField()
    end_date = models.DateField()
    capacity = models.IntegerField()
    employees = models.ManyToManyField(
        "Employee", through='TrainingProgramEmployee')

    class Meta:
        verbose_name = "training program"
        verbose_name_plural = "training programs"
