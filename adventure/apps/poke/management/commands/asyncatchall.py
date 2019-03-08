from django.core.management.base import BaseCommand, CommandError
from adventure.apps.poke.models import Pokemon, Type
import requests
import asyncio
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

        return data


    async def get_pokes_asynchronous(self):
        ##TODO improve to pokemon/?limit=151
        poke_ids = list(range(1, 152))

        with ThreadPoolExecutor(max_workers=10) as executor:
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
