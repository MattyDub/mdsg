from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
import logging
from game.models import Game
from game.game import init_game_state

logger = logging.getLogger(__name__)

@login_required
def main_view(request):
    #games = Game.objects.filter(players__contains(request.user))
    return render_to_response('index.html', {'username':request.user.username, 'games':[]},
                              context_instance=RequestContext(request))

#TODO:
#new plan: registration is distinct from game creation. All game creation is done on a single page, and only by registered users
def startgame(request):
    if request.method == 'POST':
        #TODO: DANGER NOT SANITIZED!
        address = self.request.get("address")
        logger.info('Trying to start game with email address: ' + address)
        if request.user:
            gs = game.init_game_state(request.user)
            game = Game(mapname='basic',joined=False,completed=False, state=gs)
            game.save()
            game.users.add(request.user)
        ## send_mail(subject="You're invited to play MSG!",
        ##           message="You've been invited ")
        else:
            pass #need to redirect? blow up?
        # TODO: make idempotent
        return HttpResponseRedirect('/')
    else:
        pass #TODO?

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
                              context_instance=RequestContext(request)
                              )
