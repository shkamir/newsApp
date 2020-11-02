from django.conf.urls import url
from django.urls import path

from . import views

app_name='app1'
urlpatterns = [
    url(r'^$', views.base, name='home'),
    url(r'^news$', views.news, name='news'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^search$', views.search, name='search'),
    path('register', views.register, name="register"),
    path('login', views.login_view, name="login"),
    url(r"^contact$", views.contact, name="contact"),
    url(r'^comments$', views.comment, name='comment'),
    url(r'^news/more/(?P<id>[0-9]{1,})+/(?P<title>[\w+][^/]*)$', views.more_news, name='news-query'),
    url(r'^blogs/more/(?P<id>[0-9]{1,})+/(?P<name>[\w+][^/]*)$', views.more_blogs, name='blogs-query'),
]
