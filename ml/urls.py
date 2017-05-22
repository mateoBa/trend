from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import api, views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='ml/main.html'), name='main'),
    url(r'^login/$', api.login, name='login'),
]

ml_router = SimpleRouter()
# ml_router.register(r'users', api.UserViewSet)
