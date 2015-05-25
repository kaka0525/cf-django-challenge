from django.conf.urls import include, url
from django.contrib import admin

from contact import views as contact_views

urlpatterns = [
    url(r'^$', contact_views.index, name='index'),
    url(r'^contact/', include('contact.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
