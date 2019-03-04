from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class calorieModel(models.Model):
    username = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=100, default="")
    calories = models.DecimalField(decimal_places=1, max_digits=7)
    date = models.DateField()
    CalUserForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
