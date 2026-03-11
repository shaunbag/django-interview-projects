from django.db import models
# Create your models here.

class UserBudget(models.Model):
    title = models.CharField(max_length=100)
    total = models.DecimalField(decimal_places=2, max_digits=15)


class Expenditure(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=15)