import json

from django import template

from ml.ml import ClientML

register = template.Library()
meli = ClientML(is_django=True)


@register.filter('get_publication_details')
def get_publication_details(id_publication, token):
    response = meli.get_publication(token, id_publication)
    return json.loads(response.content)
