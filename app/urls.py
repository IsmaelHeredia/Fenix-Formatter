from django.conf.urls import include, url
from app.views import home

urlpatterns = [
    url(r'^$', home.index, name='ff_home'),
    url(r'^format/$', home.format, name='ff_format'),
]