from django.core.management.base import BaseCommand, CommandError
import requests, asyncio
from concurrent.futures import ThreadPoolExecutor

from adventure.pokemons.tasks import create_poke


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
        self.stdout.write(self.style.WARNING('[{}] found!'.format(data.get('name').capitalize())))

        return {
            'name': data.get('name'),
            'id': data.get('id'),
            'types': data.get('types'),
            'sprites': data['sprites']
        }

    async def get_pokes_asynchronous(self):
        ##TODO improve to pokemon/?limit=151
        poke_ids = list(range(1, 151))

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
                for poke in await asyncio.gather(*tasks):
                    create_poke.delay(poke.get('name'), poke.get('id'), poke.get('types'), poke.get('sprites'))
                    pass

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING("\nGotta catch 'em all!\n"))

        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(self.get_pokes_asynchronous())
        loop.run_until_complete(future)

        self.stdout.write(self.style.SUCCESS("\nThat's all folks!\n"))
