from models import Game
from django import forms
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

class NewGameForm(forms.Form):
    mapname = forms.ChoiceField(choices=[('foomap','foomap'),
                                          ('barmap','barmap')])
    users = User.objects.all()
    players = forms.MultipleChoiceField(choices = [(unicode(u),unicode(u)) for u in users])

@login_required
def newgame(request):
    if request.method == 'POST':
        form = NewGameForm(request.POST)
        if form.is_valid():
            g = Game(mapname='map',joined=False, completed=False,
                     active_player=request.user)
            g.save()
            g.players.add(request.user)
            g.save()
        else:
            pass #TODO
    else:
        form = NewGameForm()
    return render_to_response('newmsggame.html',
                              {'form': form},
                              context_instance=RequestContext(request))

NEWGAME=newgame

