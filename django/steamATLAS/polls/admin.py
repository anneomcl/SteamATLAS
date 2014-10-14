from django.contrib import admin
from polls.models import Game
from polls.models import Player

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('App ID', {'fields': ['app_ID']}),
        ('Description', {'fields' : ['description']}),
        ('Price', {'fields':['price']}),
        ('Tags', {'fields':['tags']})
    ]
class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields' : ['name']})
    ]

admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)