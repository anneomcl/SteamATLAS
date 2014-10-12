from django.contrib import admin
from polls.models import Game

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('App ID', {'fields': ['app_ID']}),
        ('Description', {'fields' : ['description']}),
        ('Price', {'fields':['price']})
    ]

admin.site.register(Game, GameAdmin)