from django.conf.urls import patterns, include, url
from django.contrib import admin

from mockapp.views import document_page


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls')),
    url(r'^tweet/(?P<postid>\d+)', document_page)
)
