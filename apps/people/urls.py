from django.conf.urls import patterns, url, include
from rest_framework import routers
from apps.people import views

router = routers.DefaultRouter()
router.register(r'people', views.PersonViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls), name='people'),
    # url(r'^example-page/$', views.index, name='example-page'),
)
