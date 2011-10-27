from django.db import models
from django.db.models import Q
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
    invited_players = models.ManyToManyField(User, related_name='invited')
    players = models.ManyToManyField(User)
    active_player = models.ForeignKey(User, related_name='active')
    turn = models.IntegerField(default=1)
    units = models.ManyToManyField(Unit)
    joined = models.BooleanField()
    completed = models.BooleanField()

    def __unicode__(self):
        return self.name + ' Game #' + str(self.id)

def active_games(user):
    return Game.objects.filter(players__id=user.id, joined=True)

def waiting_games(user):
    waits = Game.objects.filter(players__id=user.id, joined=False)
    return [(unicode(w), ','.join([p.username for p in w.invited_players.all()])) for w in waits]

def invites(user):
    return Game.objects.filter(invited_players__id=user.id)
