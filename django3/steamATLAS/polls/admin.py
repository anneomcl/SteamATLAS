from django.contrib import admin
from polls.models import *
from django.db import connection

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('App ID', {'fields': ['app_ID']}),
        ('Description', {'fields' : ['description']}),
        ('Price', {'fields':['price']}),
        ('Tags', {'fields':['tags']}),
        ('score', {'fields':['score']}),
        ('Image', {'fields': ['image']})
    ]

admin.site.register(Game, GameAdmin)

class AchievementAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('description', {'fields': ['description']}),
        ('global AP', {'fields': ['globalAP']}),
        ('App ID', {'fields':['appID']})
    ]

admin.site.register(Achievement, AchievementAdmin)

class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['friends']}),
        ('lastOnline', {'fields': ['lastOnline']}),
        ('activity State', {'fields': ['activityState']}),
        ('display Name', {'fields': ['displayName']}),
        ('profile URL', {'fields': ['profileURL']}),
        ('avatar', {'fields': ['avatar']}),
        ('visibility State', {'fields': ['visibilityState']}),
        ('steam ID', {'fields':['steamID']})
    ]

admin.site.register(Player, PlayerAdmin)


class AchievedAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('steam ID', {'fields': ['steamID']}),
        ('App ID', {'fields':['app_ID']})
    ]

admin.site.register(Achieved, AchievedAdmin)

class OwnsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['totalPlaytime']}),
        ('recently Placed', {'fields': ['recentlyPlaced']}),
        ('App ID', {'fields':['appID']}),
        ('steam ID', {'fields':['steamID']})
    ]

admin.site.register(Owns, OwnsAdmin)


class GameResultsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('App ID', {'fields': ['app_ID']}),
        ('Description', {'fields' : ['description']}),
        ('Price', {'fields':['price']}),
        ('Tags', {'fields':['tags']}),
        ('score', {'fields':['score']}),
        ('Image', {'fields': ['image']})
    ]

admin.site.register(GameResults, GameResultsAdmin)







#cursor.execute('''INSERT INTO polls_Game (name, app_ID, price, tags, description) VALUES ('testergame', 100, 100, 'testertags', 'testerDescription')''')
#cursor.execute('''INSERT INTO polls_Game (name, app_ID, price, tags, description) VALUES ('testgame2', 100, 100, 'testertags', 'testerDescription')''')
'''
#cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
row = cursor.fetchone()
'''

'''4    app_ID = models.IntegerField(default=000000)
    price = models.IntegerField(default=0)
    description = models.TextField(default = "None", max_length = 1000)
    name = models.CharField(default = "None", max_length = 100)
    tags = models.TextField(default = "None", max_length = 1000)
    '''