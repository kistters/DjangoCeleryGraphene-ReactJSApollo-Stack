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
    all_pokemons = graphene.List(PokemonType,
                                 poke_name=graphene.String())

    all_types = graphene.List(TypeType,
                             type_name=graphene.String())

    def resolve_all_pokemons(self, info, **kwargs):

        poke_name = kwargs.get('poke_name')

        if poke_name is not None: 
            return Pokemon.objects.filter(name__contains=poke_name).prefetch_related('types')

        return Pokemon.objects.all().prefetch_related('types')

    def resolve_all_types(self, info, **kwargs):
        type_name = kwargs.get('type_name')

        if type_name is not None: 
            return Type.objects.filter(name__contains=type_name).prefetch_related('pokemon_set')

        return Type.objects.all().prefetch_related('pokemon_set')