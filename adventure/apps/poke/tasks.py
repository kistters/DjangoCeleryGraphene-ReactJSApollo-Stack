# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Pokemon, Type
from django.core.files.base import ContentFile
import requests


@shared_task
def create_poke(poke_name, poke_id, poke_types, poke_sprites):

    poke, poke_created = Pokemon.objects.get_or_create(
        name=poke_name,
        poke_id=poke_id)

    include_poke_sprites(poke, poke_sprites)

    if poke_created:
        include_poke_types(poke, poke_types)

    return {'name': poke.name, 'types': [poke_type.name for poke_type in poke.types.all()]}


def include_poke_types(poke, poke_types):
    for type_name in [x['type']['name'] for x in poke_types]:

        type_obj, type_created = Type.objects.get_or_create(name=type_name, )

        try:
            poke.types.add(type_obj)
        except:
            pass


def include_poke_sprites(poke, poke_sprites):
    if poke.img_shiny.name == poke.img_shiny.field.get_default():
        if poke_sprites.get('front_default', False):
            default_filename = "{}.png".format(poke.name)
            default = requests.get(poke_sprites.get('front_default'))
            poke.img_default.save(default_filename, ContentFile(default.content), save=True)

    if poke.img_shiny.name == poke.img_shiny.field.get_default():
        if poke_sprites.get('front_shiny', False):
            shiny_filename = "{}_shiny.png".format(poke.name)
            shiny = requests.get(poke_sprites.get('front_shiny'))
            poke.img_shiny.save(shiny_filename, ContentFile(shiny.content), save=True)
