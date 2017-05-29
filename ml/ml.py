from django.conf import settings

from ml_python_sdk.meli import Meli


class ClientML(object):
    def __init__(self, is_django=None):
        self.__meli = Meli(client_id=settings.CLIENT_ID, client_secret=settings.CLIENT_SECRET)
        host = settings.HOST_IP
        self.__redirect_url = '%s/trend/publications' % host if is_django else '%s/callback_from_ml' % host

    def get_params(self, token):
        self.__meli.authorize(code=token, redirect_URI=self.__redirect_url)
        return {'access_token': self.__meli.access_token}

    def get_redirect_url_to_oauth(self):
        return self.__meli.auth_url(redirect_URI=self.__redirect_url)

    def get_user_info(self, token):
        return self.__meli.get(path="/users/me", params=self.get_params(token))

    def get_publications_by_client_id(self, token, client_id):
        return self.__meli.get(path="/users/%s/items/search?status=active" % client_id,
                               params=self.get_params(token))

    def get_publication(self, token, publication_id):
        return self.__meli.get(path="/items/%s" % publication_id, params=self.get_params(token))

    def save_publication(self, token, body):
        return self.__meli.post("/items", body, params=self.get_params(token))
