from django.contrib import admin
from django.utils.html import format_html
from .models import Pokeball


class PokeballAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pokeball, PokeballAdmin)