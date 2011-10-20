from models import Game

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

