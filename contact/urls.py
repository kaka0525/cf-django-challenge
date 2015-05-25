from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^edit/(?P<user_id>\d+)$', views.edit, name='edit'),
    url(r'^save_edit/(?P<user_id>\d+)$', views.save_edit, name='save_edit'),
]
