from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
import logging

#list of game-specific modules to import
import msg

logger = logging.getLogger(__name__)

ALL_GAMES=(msg,)

@login_required
def main_view(request):
    games = []
    games.extend(msg.models.active_games(request.user))
    waiting = []
    waiting.extend(msg.models.waiting_games(request.user))
    invites = []
    invites.extend(msg.models.invites(request.user))
    return render_to_response('index.html', {'username':request.user.username,
                                             'games':games, 'waiting':waiting,
                                             'invites': invites},
                              context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user_form = form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html",
                              {'form': form},
                              context_instance=RequestContext(request))

@login_required
def newgame(request):
    form = NewGameForm()
    return render_to_response("newgame.html",
                              {'form': form},
                              context_instance=RequestContext(request))

class NewGameForm(forms.Form):
    opts = [('','Please make a selection...')]
    opts.extend([g.NEWGAME_TUPLE for g in ALL_GAMES])
    gamechoice = forms.ChoiceField(choices=opts)
