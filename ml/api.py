import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from ml import ClientML
meli = ClientML()


def login(request):
    return HttpResponse(json.dumps({'url': meli.get_redirect_url_to_oauth()}))


def callback_from_ml(request):
    request.session['token'] = request.GET.get('code')
    return HttpResponseRedirect('/#!/publications')


def get_client_data(request):
    response = meli.get_user_info(request.session['token'])
    return HttpResponse(response.content)


def get_publications(request):
    client_id = request.GET.get('client_id')
    response = meli.get_publications_by_client_id(request.session['token'], client_id)
    return HttpResponse(response.content)


def get_publication(request):
    publication_id = request.GET.get('publication_id')
    response = meli.get_publication(request.session['token'], publication_id)
    return HttpResponse(response.content)


@csrf_exempt
def save_publication(request):
    body = json.loads(request.body)
    response = meli.save_publication(request.session['token'], body)
    return HttpResponse(response.content)


def logout(request):
    request.session.flush()
    return HttpResponse()
