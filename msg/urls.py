from django.conf.urls.defaults import patterns
from views import newgame

#URLconf for individual game
urlpatterns = patterns('',
                       (r'^newgame/$', newgame),
                       )

