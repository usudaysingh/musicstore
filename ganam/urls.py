from django.conf.urls import patterns, include, url
from django.views.generic import ListView ,DetailView
from ganam.views import *
from ganam.models import ganam_songs as songs
from ganam import views
#from ganam.views import ItemListView
from django.contrib.auth import views as auth_views
#from ganam import graphs
#from ganam.views import ItemUpdateView


#ganam urls
urlpatterns=patterns('',
		     #url(r'^$',ListView.as_view(
			     #queryset=songs.objects.all().order_by("id")[:25],template_name="ganam.html")),

		     #url(r'^item_list/', ItemListView.as_view()),
		     #url(r'^item_edit_form/', ItemUpdateView.as_view()),
		     url(r'^$','django.contrib.auth.views.login'),
    		     url(r'^logout/$',logout_page),
    		     #url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    		     url(r'^register/$', register),
		     url(r'^search/$', search),
		     url(r'^view/$', vi),
    		     url(r'^register/success/$', register_success),
    		     #url(r'^home/$',ListView.as_view(queryset=songs.objects.all().order_by("id")[:25],template_name="home.html")),
		     url(r'^home/$',home),
		     #url(r'all/$','article.views.articles'),
		     url(r'^article/(?P<article_id>\d+)/$',article),
		     url(r'^delete/(?P<delete_id>\d+)/$',deleted),
		     url(r'^update/(?P<update_id>\d+)/$',update),
		     url(r'^done/(?P<done_id>\d+)/$',done),
		     url(r'^category/(?P<username>\w{0,50})/$', genre,),
		     url(r'^language/(?P<bhasha>\w{0,50})/$', language,),
		     url(r'^top_chart/(?P<music>\w{0,50})/$',top_chart),
		     url(r'^compare/(?P<comp>\w{0,50})/$',comparehj),
		     url(r'^top_language/(?P<vaani>\w{0,50})/$',top_language_chart),
		     url(r'^top_singer_chart/$',top_singer_chart),
		     url(r'^manage/$', manage),
		     #url(r'^article/$',article),
		         
		    )

