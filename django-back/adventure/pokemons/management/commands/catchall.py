from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from adventure.pokemons.models import Pokemon, Type
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

            sprites = data['sprites']

            poke, poke_created = Pokemon.objects.get_or_create(
                                    name=data['name'], 
                                    poke_id=data['id'])

            if poke_created:
                for type_name in [x['type']['name'] for x in data['types']]:
                    type_obj, type_created = Type.objects.get_or_create(name=type_name,)
                    if type_created:
                        self.stdout.write('type [{}] included.'.format(type_obj.name))
                        
                    poke.types.add(type_obj)

                if sprites.get('front_default', False):
                    res_default = requests.get(sprites.get('front_default'))
                    default_filename = "{}.png".format(poke.name)
                    poke.img_default.save(default_filename, ContentFile(res_default.content), save=False)

                if sprites.get('front_shiny', False):
                    res_shiny = requests.get(sprites.get('front_shiny'))
                    shiny_filename = "{}_shiny.png".format(poke.name)
                    poke.img_shiny.save(shiny_filename, ContentFile(res_shiny.content), save=False)

                poke.save()

                self.stdout.write(self.style.SUCCESS('[{}] captured!'.format(poke.name.capitalize())))
            else:
                self.stdout.write('[{}] has already been caught!'.format(poke.name.capitalize()))
