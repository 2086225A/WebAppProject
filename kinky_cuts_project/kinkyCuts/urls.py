from django.conf.urls import patterns,url
from kinkyCuts import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^explore/$', views.explore, name='explore'),
    url(r'^mypictures/$', views.mypictures, name='mypictures'),
    url(r'^myaccount/$', views.myaccount, name='myaccount'),
    url(r'^edit_profile/$', views.editProfile, name='edit_profile'),
    )
