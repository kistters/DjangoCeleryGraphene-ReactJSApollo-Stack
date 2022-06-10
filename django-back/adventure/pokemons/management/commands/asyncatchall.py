from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from adventure.pokemons.models import Pokemon, Type
import requests, asyncio
from concurrent.futures import ThreadPoolExecutor


class Command(BaseCommand):
    help = 'Catch all 150 pokes :)'

    poke_types = {}

    def catch(self, session, poke_id):
        endpoint = "https://pokeapi.co/api/v2/pokemon/{}/".format(poke_id)

        response = session.get(endpoint)
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR('- fail calling {}'.format(endpoint)))
            return False

        data = response.json()
        sprites = data['sprites']
        poke_sprites = {}

        if sprites.get('front_default', False):
            poke_sprites['default'] = requests.get(sprites.get('front_default'))

        if sprites.get('front_shiny', False):
            poke_sprites['shiny'] = requests.get(sprites.get('front_shiny'))

        self.stdout.write(self.style.WARNING('[{}] found!'.format(data.get('name').capitalize())))

        return {
            'name': data.get('name'),
            'id': data.get('id'),
            'types': data.get('types'),
            'sprites': poke_sprites
        }

    def create_poke(self, pokedata):

        poke_types = pokedata['types']
        poke_sprites = pokedata['sprites']

        poke, poke_created = Pokemon.objects.get_or_create(
                                    name=pokedata['name'], 
                                    poke_id=pokedata['id'])

        self.include_poke_sprites(poke, poke_sprites)

        if poke_created:
            self.include_poke_types(poke, poke_types)
            self.stdout.write(self.style.SUCCESS('[{}] captured!'.format(poke.name.capitalize())))
        else:
            self.stdout.write('[{}] has already been caught!'.format(poke.name.capitalize()))

    def include_poke_types(self, poke, poke_types):
        for type_name in [x['type']['name'] for x in poke_types]:

            type_obj, type_created = Type.objects.get_or_create(name=type_name,)
            if type_created:
                self.stdout.write('type [{}] included.'.format(type_obj.name))

            if not self.poke_types.get(type_obj.name, False):
                self.poke_types[type_obj.name] = type_obj

            try:
                poke.types.add(self.poke_types.get(type_name, None))
                self.stdout.write(self.style.WARNING("Poke {} is the [{}] type".format(poke.name, type_name)))
            except:
                self.stdout.write(self.style.ERROR("faill add types to {}".format(poke.name)))

    def include_poke_sprites(self, poke, poke_sprites):

        if poke.img_shiny.name == poke.img_shiny.field.get_default():
            if poke_sprites.get('default', False):
                default_filename = "{}.png".format(poke.name)
                default = poke_sprites.get('default', False)
                poke.img_default.save(default_filename, ContentFile(default.content), save=True)

        if poke.img_shiny.name == poke.img_shiny.field.get_default():
            if poke_sprites.get('shiny', False):
                shiny_filename = "{}_shiny.png".format(poke.name)
                shiny = poke_sprites.get('shiny', False)
                poke.img_shiny.save(shiny_filename, ContentFile(shiny.content), save=True)
        
    async def get_pokes_asynchronous(self):
        ##TODO improve to pokemon/?limit=151
        poke_ids = list(range(1, 152))

        with ThreadPoolExecutor(max_workers=50) as executor:
            with requests.Session() as session:
                # Set any session parameters here before calling `catch`
                loop = asyncio.get_event_loop()
                tasks = [
                    loop.run_in_executor(
                        executor,
                        self.catch,
                        *(session, poke_id) # Allows us to pass in multiple arguments to `catch`
                    )
                    for poke_id in poke_ids
                ]
                for pokedata in await asyncio.gather(*tasks):
                    self.create_poke(pokedata)
                    pass

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING("\nGotta catch 'em all!\n"))

        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(self.get_pokes_asynchronous())
        loop.run_until_complete(future)
        
        self.stdout.write(self.style.SUCCESS("\nThat's all folks!\n"))

       
