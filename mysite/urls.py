from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^polls/', include('mysite.polls.urls')),
    (r'^admin/', include(admin.site.urls)),
)