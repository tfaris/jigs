from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',    
    url(r'^start/([\-a-f0-9]+)/$','puzzle.views.start_puzzle_session'),
    url(r'^([\-a-f0-9]+)/$', 'puzzle.views.workon_session', name='puzzle'),
    url(r'^([\-a-f0-9]+)/status/$', 'puzzle.views.session_status'),
)
