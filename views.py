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
import game

logger = logging.getLogger(__name__)

@login_required
def main_view(request):
    games = []
    games.extend(game.models.listgames(request.user))
    return render_to_response('index.html', {'username':request.user.username, 'games':games},
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
                              context_instance=RequestContext(request)
                              )
