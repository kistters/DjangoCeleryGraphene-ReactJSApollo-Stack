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
        poke_queryset = Pokemon.objects.all().prefetch_related('types').exclude(enable=False)
        
        if poke_name is not None:
            return poke_queryset.filter(name__contains=poke_name)

        return poke_queryset

    def resolve_all_types(self, info, **kwargs):
        type_name = kwargs.get('type_name')
        type_queryset = Type.objects.all().prefetch_related('pokemon_set')

        if type_name is not None: 
            return type_queryset.filter(name__contains=type_name)

        return type_queryset