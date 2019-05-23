from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=64, blank=False, unique=True)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=64, blank=False, unique=True)
    types = models.ManyToManyField(Type)
    poke_id = models.IntegerField(unique=True, default=None)
    img_default = models.ImageField(upload_to='pokes/',)
    img_shiny = models.ImageField(upload_to='pokes/',)
    enable = models.BooleanField(default=True)

    class Meta:
        ordering = ['-poke_id']

    def __str__(self):
        return self.name
