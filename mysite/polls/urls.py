from django.conf.urls import url

from . import views


# If you want to change the URL of the polls detail view
# to something else, perhaps to something like polls/specifics/12/
# instead of doing it in the template
# (or templates) you would change it in polls/urls.py
# ie. url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),


# Namespacing URL names
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]