import json

from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView

from ml.ml import ClientML
from ml_django.forms import CreatePublicationForm

meli = ClientML(is_django=True)


def login(request):
    return HttpResponseRedirect(meli.get_redirect_url_to_oauth())


class Publications(TemplateView):
    template_name = 'ml_django/publications.html'

    def get(self, request, *args, **kwargs):
        if request.GET.get('code'):
            request.session['token'] = request.GET.get('code')
        return super(Publications, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Publications, self).get_context_data(**kwargs)
        user_data = json.loads(meli.get_user_info(self.request.session['token']).content)
        publications = json.loads(meli.get_publications_by_client_id(self.request.session['token'],
                                                                     user_data.get('id')).content)['results']
        publications.reverse()
        context['user'] = user_data
        context['publications'] = publications
        context['token'] = self.request.session['token']
        return context


class CreatePublication(FormView):
    form_class = CreatePublicationForm
    template_name = 'ml_django/create_publication.html'
    success_url = reverse_lazy('trend_django:publications')

    def form_valid(self, form):
        form.save(self.request.session['token'])
        return super(CreatePublication, self).form_valid(form)


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('trend_django:main'))
