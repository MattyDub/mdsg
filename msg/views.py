from django.http import HttpResponseRedirect
from models import Game
from django import forms
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

class NewGameForm(forms.Form):
    mapname = forms.ChoiceField(choices=[('foomap','foomap'),
                                          ('barmap','barmap')])
    players = forms.MultipleChoiceField()

    def __init__(self, *args, **kwargs):
        exclude_user = kwargs.pop('exclude_user')
        super(NewGameForm ,self).__init__(*args, **kwargs)
        self.fields['players'].choices = [(unicode(u),unicode(u)) for u in User.objects.exclude(id=exclude_user)]

@login_required
def newgame(request):
    if request.method == 'POST':
        form = NewGameForm(request.POST, exclude_user=request.user.id)
        if form.is_valid():
            cd = form.cleaned_data
            print cd['players']
            g = Game(mapname = cd['mapname'],
                     joined=False, completed=False,
                     active_player=request.user)
            g.save()
            g.players.add(request.user)
            for u in User.objects.filter(username__in=cd['players']):
                g.invited_players.add(u)
            g.save()
            return HttpResponseRedirect("/")
        else:
            pass #TODO
    else:
        form = NewGameForm(exclude_user=request.user.id)
    return render_to_response('newmsggame.html',
                              {'form': form},
                              context_instance=RequestContext(request))

@login_required
def joingame(request, game_id):
    logger.info("User " + request.user.username + " trying to join game " + game_id)
    game = Game.objects.filter(id=game_id)
    #TODO: pick up here
    if request.user in game.invited_players:
        game.players.add(request.user)
        game.invited_players.remove(request.user)
    else:
        pass #TODO: trying to join a game uninvited

NEWGAME='/MSG/newgame/'

