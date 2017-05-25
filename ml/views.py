# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class MLView(TemplateView):
    template_name = 'ml/publications.html'

    def get(self, request, *args, **kwargs):
        self.request.session['token'] = request.GET.get('code')
        self.request.session['error'] = request.GET.get('error')
        self.request.session['error_description'] = request.GET.get('error_description')
        return super(MLView, self).get(request, *args, **kwargs)
