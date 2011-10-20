from django.db import models
from django.contrib.auth.models import User

class Unit(models.Model):
    player = models.ForeignKey(User)
    xpos = models.IntegerField()
    ypos = models.IntegerField()
    unit_type = models.CharField(max_length=30) # or do we want this in another table?

class GameState(models.Model):
    active_player = models.ForeignKey(User)
    turn = models.IntegerField()
    units = models.ManyToManyField(Unit)

class Game(models.Model):
    mapname = models.CharField(max_length=20)
    players = models.ManyToManyField(User)
    state = models.ForeignKey(GameState)
    joined = models.BooleanField()
    completed = models.BooleanField()
