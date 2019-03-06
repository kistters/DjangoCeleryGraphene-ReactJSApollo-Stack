from django.contrib import admin
from . import models

class PokeAdmin(admin.ModelAdmin):
    pass

class TypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Pokemon, PokeAdmin)
admin.site.register(models.Type, TypeAdmin)