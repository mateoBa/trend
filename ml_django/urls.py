from django.conf.urls import url
from django.views.generic import TemplateView

from ml_django import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='ml_django/main.html'), name='main'),
    url(r'^login/$', views.login, name='login'),
    url(r'^publications/$', views.Publications.as_view(), name='publications'),
    url(r'^create_publication/$', views.CreatePublication.as_view(), name='create_publication'),
    url(r'^logout/$', views.logout, name='logout')
]
