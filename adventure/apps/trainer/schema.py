import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from .models import Pokeball

class TrainerType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class PokeballType(DjangoObjectType):
    class Meta:
        model = Pokeball

class Query(object):
    all_trainers = graphene.List(TrainerType,)
    all_pokeballs = graphene.List(PokeballType,)

    def resolve_all_trainers(self, info, **kwargs):
        return get_user_model().objects.all().prefetch_related('pokeballs')

    def resolve_all_pokeballs(self, info, **kwargs):
        return Pokeball.objects.all().select_related('poke').select_related('owner')