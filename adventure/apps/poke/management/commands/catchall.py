from django.core.management.base import BaseCommand, CommandError
from adventure.apps.poke.models import Pokemon, Type
import requests

class Command(BaseCommand):
    help = 'Catch all 150 pokes :)'

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING("\nGotta catch 'em all!\n"))

        ##TODO improve to pokemon/?limit=151
        for idx in range(1, 152):
            url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(idx)

            r = requests.get(url)
            ##TODO validate body response 
            data = r.json()

            poke = {
                "name": data['name'],
                "types": [x['type']['name'] for x in data['types']]
            }

            pokeObj, poke_created = Pokemon.objects.get_or_create(name=poke['name'],)

            if poke_created:
                for type_name in poke['types']:
                    typeObj, type_created = Type.objects.get_or_create(name=type_name,)

                    pokeObj.types.add(typeObj)
        
                self.stdout.write(self.style.SUCCESS('[{}] captured!'.format(pokeObj.name.capitalize())))
            else:
                self.stdout.write('[{}] has already been caught!'.format(pokeObj.name.capitalize()))

            # try:
            #     pokemon = models.Pokemon.objects.get(name=data['name'])
            # except models.Pokemon.DoesNotExist:
            #     pokemon = models.Pokemon(name=data['name'])
            #     pokemon.save()
            #
            # for type_name in poke['types']:
            #     try:
            #         typeName = models.Type.objects.get(name=type_name)
            #     except models.Type.DoesNotExist:
            #         typeName = models.Type(name=type_name)
            #         typeName.save()
            #
            #     pokemon.types.add(typeName)
