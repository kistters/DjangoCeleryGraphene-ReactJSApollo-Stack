from django.db import models



class Type(models.Model):
    name = models.CharField(max_length=64, blank=False, unique=True)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=64, blank=False, unique=True)
    types = models.ManyToManyField(Type)

    def __str__(self):
        return self.name