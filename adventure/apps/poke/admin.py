from django.contrib import admin
from django.utils.html import format_html
from . import models

class PokeAdmin(admin.ModelAdmin):
    list_display = ('poke_id', 'poke_name', 'images',)
    search_fields = ('id', 'poke_id', 'name',)
    list_filter = ('types',)
    readonly_fields = ['images', 'poke_id', 'types',]

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

class TypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Pokemon, PokeAdmin)
admin.site.register(models.Type, TypeAdmin)