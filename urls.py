from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from djmsg.views import main_view, register, newgame
from django.conf import settings
import msg

admin.autodiscover()

urlpatterns = patterns('',
                       (r'^accounts/login/$', login, {'template_name':'login.html'}),
                       (r'^accounts/logout/$', logout, {'template_name':'login.html'}),
                       (r'^register/$', register),
                       (r'^$', main_view),
                       (r'^newgame/$', newgame),
                       (r'^msg/', include('msg.urls')),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
#                       (r'^static/(?P<path>.*)$', 'django.views.static.serve',
#                        {'document_root': settings.STATIC_DIR}),
    #(r'^$', login, {'template_name':'login.html'}),
    # Examples:
    # url(r'^$', 'djmsg.views.home', name='home'),
    # url(r'^djmsg/', include('djmsg.foo.urls')),
)
