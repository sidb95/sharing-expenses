from django.db import models


class Person(models.Model):
    uuid = models.IntegerField(auto_created=True, unique=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    contact = models.IntegerField()
    total = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
