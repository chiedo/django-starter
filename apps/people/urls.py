from django.conf.urls import patterns, url

from apps.people import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'^example-page/$', views.index, name='example-page'),
)
