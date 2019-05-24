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
            'types__name': ['iexact', 'icontains', 'istartswith']
        }
        exclude_fields = {
            'enable'
        }

    img_default_field = graphene.String()

    def resolve_img_default_field(self, resolve):
        return resolve.context.build_absolute_uri(self.img_default and self.img_default.url)


class TypeType(DjangoObjectType):
    class Meta:
        model = Type
        interfaces = (graphene.Node, )
        filter_fields = {
            'name': ['iexact', 'icontains', 'istartswith'],
        }


class Query(object):

    all_pokemons = DjangoFilterConnectionField(PokemonType)
    all_types = DjangoFilterConnectionField(TypeType)

    @staticmethod
    def resolve_all_pokemons(self, info, **kargs):
        """" graphene_django/fields.py: merge_querysets """
        return Pokemon.objects.all().exclude(enable=False)
