from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.home.urls')),
    url(r'^api/', include('apps.people.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # May not be necessary for production environment?
    # Bridge will be crossed once we get there
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}),
    # Pass anything else to the reactjs router. Must be last
    url(r'^.*$', 'apps.home.views.index')
)
