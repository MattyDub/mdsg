from django.conf.urls.defaults import patterns
from views import newgame, joingame

#URLconf for individual game
urlpatterns = patterns('',
                       (r'^newgame/$', newgame),
                       (r'^joingame/(?P<game_id>\d+)$', joingame),
                       )

