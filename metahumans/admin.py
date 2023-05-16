from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import Team, Power, Metahuman


class PowerAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )
    list_display = ('id', 'name')


admin.site.register(Power, PowerAdmin)


class TeamAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
        'headquarter',
    )
    list_display = ('id', 'name', 'headquarter')


admin.site.register(Team, TeamAdmin)


class MetahumanAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
        'team__name',
    )
    list_display = (
        'id',
        'name',
        'num_powers',
        'danger_level',
        'in_team',
        'photo',
    )
    list_filter = (
        'team',
        'level',
    )
    exclude = ('is_active',)

    def danger_level(self, mh):
        if mh.level <= 50:
            return format_html(f"<strong>{mh.level}</strong>")
        else:
            return str(mh.level)

    def in_team(self, mh):
        return mh.team.exists()

    in_team.boolean = True


admin.site.register(Metahuman, MetahumanAdmin)
