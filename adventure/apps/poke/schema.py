import graphene

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import Pokemon, Type

class PokemonType(DjangoObjectType):
    class Meta:
        model = Pokemon
        interfaces = (graphene.Node, )
        filter_fields = {
            'poke_id': ['exact'],
            'name': ['iexact', 'icontains', 'istartswith'],
            'enable': ['exact'],
        }

class TypeType(DjangoObjectType):
    class Meta:
        model = Type
        interfaces = (graphene.Node, )
        filter_fields = {
            'name': ['iexact', 'icontains', 'istartswith'],
        }

class Query(object):

    pokemon = graphene.Node.Field(PokemonType)
    all_pokemons = DjangoFilterConnectionField(PokemonType)

    type = graphene.Node.Field(TypeType)
    all_types = DjangoFilterConnectionField(TypeType)