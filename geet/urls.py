from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geet.views.home', name='home'),
    # url(r'^geet/', include('geet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^ganam/', include('ganam.urls')),
    url(r'^admin/', include(admin.site.urls)),
     url(r'^accounts/login/$', auth_views.login),    
)
