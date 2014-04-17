from django.conf.urls import patterns, include, url

from django.contrib import admin
from dooropener.views import text_from_twilio

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GarageDoorOpener.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^text_received/', text_from_twilio),
)
