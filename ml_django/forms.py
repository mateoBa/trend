import json

from django import forms

from ml.ml import ClientML

meli = ClientML(is_django=True)


class CreatePublicationForm(forms.Form):
    title = forms.CharField(label='Titulo', max_length=100)
    description = forms.CharField(label='Description', max_length=500, widget=forms.Textarea, required=False)
    price = forms.IntegerField(label='Precio')
    stock = forms.IntegerField(label='Cantidad')
    imagen1 = forms.URLField(label='Imagen', max_length=100)
    imagen2 = forms.URLField(label='Imagen Complementaria', max_length=100, required=False)

    def save(self, token):
        title = self.cleaned_data['title']
        description = self.cleaned_data['description']
        price = self.cleaned_data['price']
        stock = self.cleaned_data['stock']
        imagen1 = self.cleaned_data['imagen1']
        imagen2 = self.cleaned_data['imagen2']
        pictures = [{'source': imagen1}]
        if imagen2:
            pictures.append({'source': imagen2})
        body = {'title': title, 'description': description, 'price': price, 'currency_id': 'ARS', 'condition': 'new',
                'available_quantity': stock, 'pictures': pictures, 'category_id': 'MLA352543',
                'listing_type_id': 'bronze'}
        content = json.loads(meli.save_publication(token, body).content)
        if content.get('status') != 'active':
            raise forms.ValidationError(content)
