from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from djmsg.views import main_view, startgame, register
from django.conf import settings

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       (r'^accounts/login/$', login, {'template_name':'login.html'}),
                       (r'^accounts/logout/$', logout, {'template_name':'login.html'}),
                       (r'^$', main_view),
                       (r'^startgame/$', startgame),
                       (r'^register/', register),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
#                       (r'^static/(?P<path>.*)$', 'django.views.static.serve',
#                        {'document_root': settings.STATIC_DIR}),
    #(r'^$', login, {'template_name':'login.html'}),
    # Examples:
    # url(r'^$', 'djmsg.views.home', name='home'),
    # url(r'^djmsg/', include('djmsg.foo.urls')),
)
