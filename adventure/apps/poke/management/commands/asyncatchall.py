from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from adventure.apps.poke.models import Pokemon, Type
import requests, asyncio
from concurrent.futures import ThreadPoolExecutor


class Command(BaseCommand):
    help = 'Catch all 150 pokes :)'

    def catch(self, session, poke_id):
        endpoint = "https://pokeapi.co/api/v2/pokemon/{}/".format(poke_id)

        response = session.get(endpoint)
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR('- fail calling {}'.format(endpoint)))
            return False

        data = response.json()

        poke_types = data['types']
        poke_sprites = data['sprites']

        poke, poke_created = Pokemon.objects.get_or_create(
                                    name=data['name'], 
                                    poke_id=data['id'])

        self.include_poke_sprites(poke, poke_sprites)

        if poke_created:
            self.include_poke_types(poke, poke_types)

            self.stdout.write(self.style.SUCCESS('[{}] captured!'.format(poke.name.capitalize())))
        else:
            self.stdout.write('[{}] has already been caught!'.format(poke.name.capitalize()))

        return poke

    def include_poke_types(self, poke, poke_types):
        types_list = []
        for type_name in [x['type']['name'] for x in poke_types]:
            type_obj, type_created = Type.objects.get_or_create(name=type_name,)
            if type_created:
                self.stdout.write('type [{}] included.'.format(type_obj.name))
            types_list.append(type_obj)

        try:
            poke.types.set(types_list)
        except:
          print("faill add types to {}".format(poke.name))

    def include_poke_sprites(self, poke, poke_sprites):
        if poke.img_shiny.name == poke.img_shiny.field.get_default():
            if poke_sprites.get('front_default', False):
                res_default = requests.get(poke_sprites.get('front_default'))
                default_filename = "{}.png".format(poke.name)
                poke.img_default.save(default_filename, ContentFile(res_default.content), save=True)

        if poke.img_shiny.name == poke.img_shiny.field.get_default():
            if poke_sprites.get('front_shiny', False):
                res_shiny = requests.get(poke_sprites.get('front_shiny'))
                shiny_filename = "{}_shiny.png".format(poke.name)
                poke.img_shiny.save(shiny_filename, ContentFile(res_shiny.content), save=True)


    async def get_pokes_asynchronous(self):
        ##TODO improve to pokemon/?limit=151
        poke_ids = list(range(1, 152))

        with ThreadPoolExecutor(max_workers=20) as executor:
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
                for response in await asyncio.gather(*tasks):
                    pass

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING("\nGotta catch 'em all!\n"))

        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(self.get_pokes_asynchronous())
        loop.run_until_complete(future)
        
        self.stdout.write(self.style.SUCCESS("\nThat's all folks!\n"))

       
