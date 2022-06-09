from django.contrib import admin
from django.utils.html import format_html
from . import models


class PokeAdmin(admin.ModelAdmin):
    list_display = ('poke_id', 'poke_name', 'images', 'enable',)
    search_fields = ('id', 'poke_id', 'name',)
    list_filter = ('types', 'enable',)
    readonly_fields = ['images', 'poke_id', 'types',]
    actions = ['disable_poke', ]

    def images(self, obj):
        return format_html("""
            <img src="{default}" width="62" height="62" />
            <img src="{shiny}" width="62" height="62" />
            """.format(
                default=obj.img_default.url,
                shiny=obj.img_shiny.url
                )
            )

    def poke_name(self, obj):
        return obj.name.capitalize()

    def disable_poke(modelAdmin, request, queryset):
        queryset.update(enable=False)

    disable_poke.short_description = 'Disable selected pokemons'

class TypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Pokemon, PokeAdmin)
admin.site.register(models.Type, TypeAdmin)