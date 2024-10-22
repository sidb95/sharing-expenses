from django.db import models


class Expense(models.Model):
    uuid = models.IntegerField(auto_created=True, unique=True)
    amount = models.IntegerField()
    users_expense = models.JSONField()
