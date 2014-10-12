from django.contrib import admin
from polls.models import Game

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('App ID', {'fields': ['app_ID']}),
        ('Description', {'fields' : ['description']}),
        ('Price', {'fields':['price']}),
        ('Tags', {'fields':['tags']})
    ]

admin.site.register(Game, GameAdmin)