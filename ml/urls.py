from django.conf.urls import url
from django.views.generic import TemplateView

from . import api

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='ml/main.html'), name='main'),
    url(r'^login/$', api.login, name='login'),
    url(r'^callback_from_ml/$', api.callback_from_ml, name='callback_from_ml'),
    url(r'^get_client_data/$', api.get_client_data, name='get_client_data'),
    url(r'^get_publications/$', api.get_publications, name='get_publications'),
    url(r'^get_publication/$', api.get_publication, name='get_publication'),
    url(r'^save_publication/$', api.save_publication, name='save_publication'),
    url(r'^logout/$', api.logout, name='logout')
]

