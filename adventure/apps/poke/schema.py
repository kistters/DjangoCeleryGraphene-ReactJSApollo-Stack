import graphene

from graphene_django.types import DjangoObjectType
from .models import Pokemon, Type

class PokemonType(DjangoObjectType):
    class Meta:
        model = Pokemon

class TypeType(DjangoObjectType):
    class Meta:
        model = Type

class Query(object):
    all_pokemons = graphene.List(PokemonType)
    all_types = graphene.List(TypeType)

    def resolve_all_pokemons(self, info, **kwargs):
        return Pokemon.objects.prefetch_related('types').all()

    def resolve_all_types(self, info, **kwargs):
        return Type.objects.prefetch_related('pokemon_set').all()