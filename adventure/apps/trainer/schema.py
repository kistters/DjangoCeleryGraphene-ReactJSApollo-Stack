from django.contrib.auth import get_user_model

import graphene
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
            'id': ['exact'],
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
    me = graphene.Field(TrainerType)
    all_trainers = DjangoFilterConnectionField(TrainerType,)
    all_pokeballs = DjangoFilterConnectionField(PokeballType,)

    @staticmethod
    def resolve_me(self, info, **kargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user

    @staticmethod
    def resolve_all_trainers(self, info, **kargs):
        return get_user_model().objects.all().prefetch_related('pokeballs')

    @staticmethod
    def resolve_all_pokeballs(self, info, **kargs):
        return Pokeball.objects.all().select_related('poke').select_related('owner')


class TrainerInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)
    email = graphene.String(required=True)


class CreateTrainer(graphene.Mutation):
    class Arguments:
        input = TrainerInput()

    ok = graphene.Boolean()
    trainer = graphene.Field(TrainerType)

    @staticmethod
    def mutate(root, resolve, input=None):
        ok = True
        trainer_instance = get_user_model()(
            username=input.username,
            email=input.email
        )
        trainer_instance.set_password(input.password)
        trainer_instance.save()
        return CreateTrainer(ok=ok, trainer=trainer_instance)


class Mutation(graphene.ObjectType):
    create_trainer = CreateTrainer.Field()
