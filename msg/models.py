from django.db import models
from django.contrib.auth.models import User

GAMENAME='MSG'

class Unit(models.Model):
    player = models.ForeignKey(User)
    xpos = models.IntegerField()
    ypos = models.IntegerField()
    unit_type = models.CharField(max_length=30) # or do we want this in another table?

class Game(models.Model):
    name = models.CharField(max_length=50, default=GAMENAME)
    mapname = models.CharField(max_length=20)
    players = models.ManyToManyField(User)
    active_player = models.ForeignKey(User, related_name='active')
    turn = models.IntegerField(default=1)
    units = models.ManyToManyField(Unit)
    joined = models.BooleanField()
    completed = models.BooleanField()

    def __unicode__(self):
        return self.name + ' Game #' + str(self.id)

def listgames(user):
    return Game.objects.filter(players__id=user.id)
