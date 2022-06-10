from django.core.management.base import BaseCommand, CommandError
from adventure.pokemons.models import Pokemon, Type

class Command(BaseCommand):
    help = 'Find pokes'

    def add_arguments(self, parser):
        parser.add_argument('poke_name', nargs='+', type=str)

    def handle(self, *args, **options):
        for poke_name in options['poke_name']:

            pokesQuerySet = Pokemon.objects.filter(name__contains=poke_name)

            if not pokesQuerySet.exists():
                self.stdout.write(self.style.WARNING('[{}] has not been caught!'.format(poke_name)))
            else:
                for poke in pokesQuerySet:
                    self.stdout.write(self.style.SUCCESS('[{}] has already been caught!'.format(poke.name.capitalize())))

