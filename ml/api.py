from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import generics, viewsets, serializers, status
from rest_framework.response import Response
from django.conf import settings

import sys
sys.path.append('%s/lib/python-sdk/lib' % settings.BASE_DIR)
from meli import Meli


def login(request):
    meli = Meli(client_id=settings.CLIENT_ID, client_secret=settings.CLIENT_SECRET)
    return HttpResponseRedirect(meli.auth_url(redirect_URI=settings.REDIRECT_URL))

