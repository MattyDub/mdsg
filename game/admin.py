from django.contrib import admin
from djmsg.game.models import Game, Unit, GameState

admin.site.register(Game)
admin.site.register(Unit)
admin.site.register(GameState)
