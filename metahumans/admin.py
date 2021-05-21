from django.contrib import admin

# Register your models here.

from .models import Equipo, Poder, Metahumano

class PoderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Poder, PoderAdmin)

class EquipoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Equipo, EquipoAdmin)

class MetahumanoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Metahumano, MetahumanoAdmin)

