from django.db import models
from django.contrib.auth.models import User
from adventure.apps.poke.models import Pokemon


class Pokeball(models.Model):
    """where trainer's pokemon are."""

    name = models.CharField(max_length=64, blank=False,)
    poke = models.ForeignKey(Pokemon, on_delete=models.PROTECT, to_field='poke_id')
    # poke = models.ForeignKey('poke.Pokemon', on_delete=models.DO_NOTHING, to_field='poke_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pokeballs')

    def __str__(self):
        return "PokeName: {} Especie: {}  Owner: {}".format(self.name, self.poke_id, self.owner)
