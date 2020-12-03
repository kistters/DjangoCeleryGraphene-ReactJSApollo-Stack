from django.core.management.base import BaseCommand

from adventure.apps.poke.models import Pokemon
from adventure.apps.poke.schema import PokeEvent
import time


class Command(BaseCommand):
    help = 'Notify pokes'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for poke in Pokemon.objects.all().order_by("?").prefetch_related('types'):
            time.sleep(.2)
            for poke_type in poke.types.all():
                print(poke_type, poke.name)
                PokeEvent.broadcast(group=f'poke_event_{poke_type}', payload={'pokemon': poke})

        print('again')
        self.handle(*args, **options)
