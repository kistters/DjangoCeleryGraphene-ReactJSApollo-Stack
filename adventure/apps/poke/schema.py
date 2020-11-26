import channels_graphql_ws
import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django.conf import settings
from .models import Pokemon, Type


def get_absolute_url(path=None):
    if not path:
        return settings.DOMAIN
    return f'//{settings.DOMAIN}{path}'


class PokemonType(DjangoObjectType):
    class Meta:
        model = Pokemon
        interfaces = (graphene.Node,)
        filter_fields = {
            'poke_id': ['exact'],
            'name': ['iexact', 'icontains', 'istartswith'],
            'types__name': ['iexact', 'icontains', 'istartswith']
        }
        exclude_fields = ('enable',)

    img_default_field = graphene.String()

    def resolve_img_default_field(self, info, *args, **kwds):
        return get_absolute_url(self.img_default and self.img_default.url)


class TypeType(DjangoObjectType):
    class Meta:
        model = Type
        interfaces = (graphene.Node,)
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


class PokeEvent(channels_graphql_ws.Subscription):
    """Simple GraphQL subscription."""

    # Subscription payload.
    event = graphene.String()
    pokemon = graphene.Field(PokemonType)

    class Arguments:
        """That is how subscription arguments are defined."""
        track_poke_types = graphene.List(graphene.String)

    @staticmethod
    def subscribe(root, info, track_poke_types):
        """Called when user subscribes."""

        return [f'poke_event_{poke_type}' for poke_type in track_poke_types]

    @staticmethod
    def publish(payload, info, track_poke_types):
        poke = payload.get('pokemon')
        return PokeEvent(pokemon=poke, event=f'pokemon: {poke.name.title()}!')


class Subscription(object):
    poke_event = PokeEvent.Field()
