from django.contrib import admin
from werewolf.models import Character, Game, GameMembership

# Register your models here.
admin.site.register(Character)
admin.site.register(Game)
admin.site.register(GameMembership)