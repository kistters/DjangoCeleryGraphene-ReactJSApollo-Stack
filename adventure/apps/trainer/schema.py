import graphene

from django.contrib.auth import get_user_model

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Pokeball


class TrainerType(DjangoObjectType):
    """
        Trainer -> User
    """
    class Meta:
        model = get_user_model()
        interfaces = (graphene.Node, )
        filter_fields = {
            'email': ['iexact', 'icontains', 'istartswith'],
            'username': ['iexact', 'icontains', 'istartswith'],
            'first_name': ['iexact', 'icontains', 'istartswith'],
            'last_name': ['iexact', 'icontains', 'istartswith'],
            'is_active': ['exact'],
        }


class PokeballType(DjangoObjectType):
    class Meta:
        model = Pokeball
        interfaces = (graphene.Node,)
        filter_fields = {
            'name': ['iexact', 'icontains', 'istartswith'],
            'poke': ['exact'],
            'poke__name': ['iexact', 'icontains', 'istartswith'],
        }


class Query(object):
    # all_pokemons = DjangoFilterConnectionField(PokemonType)
    all_trainers = DjangoFilterConnectionField(TrainerType,)
    all_pokeballs = DjangoFilterConnectionField(PokeballType,)

    @staticmethod
    def resolve_all_trainers(self, info, **kargs):
        return get_user_model().objects.all().prefetch_related('pokeballs')

    @staticmethod
    def resolve_all_pokeballs(self, info, **kargs):
        return Pokeball.objects.all().select_related('poke').select_related('owner')
