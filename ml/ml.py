from django.conf import settings

from ml_python_sdk.meli import Meli


class ClientML(object):
    def __init__(self):
        self.__meli = Meli(client_id=settings.CLIENT_ID, client_secret=settings.CLIENT_SECRET)
        self.__access_token = None
        self.__token = None

    def set_token(self, token):
        self.__token = token

    def get_params(self):
        self.__access_token = self.__meli.authorize(code=self.__token, redirect_URI=settings.REDIRECT_URL)
        return {'access_token': self.__meli.access_token}

    def get_redirect_url_to_oauth(self):
        return self.__meli.auth_url(redirect_URI=settings.REDIRECT_URL)

    def get_user_info(self):
        return self.__meli.get(path="/users/me", params=self.get_params())

    def get_publications_by_client_id(self, client_id):
        return self.__meli.get(path="/users/%s/items/search?status=active" % client_id,
                               params=self.get_params())

    def get_publication(self, publication_id):
        return self.__meli.get(path="/items/%s" % publication_id, params=self.get_params())

    def save_publication(self, body):
        return self.__meli.post("/items", body, params=self.get_params())
