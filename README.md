# Trend

Proyecto test para [Real Trends](http://www.real-trends.com/ar/), con este vas a poder crear y ver publicaciones activas en [Mercado Libre](https://www.mercadolibre.com.ar/).

Este proyecto cuenta con 2 aplicaciones:

  - http://localhost:8000 backend Django y cliente web hecho con Angular.
  - http://localhost:8000/trend aplicación hecha en Django.

Las 2 aplicaciones tienen funcionalidades similares.


### Installation

```sh
$ cd trend
$ pip install -r requirements.txt
```

Trend requiere [Bower.js](https://bower.io/) para installar las librerias.

Para instalar librerias externas.

```sh
$ bower install bower.json
```

### Configuración de trend/settings.py

Como último paso, debemos crear una aplicación en Mercado Libre para obtener el CLIENT_ID y el CLIENT_SECRET que serán seteados en el archivo trend/settings.py.

[Crear Aplicaiones](http://developers.mercadolibre.com.ar/apps)

Cuando nos pide que completemos el campo Redirect URI colamos http://localhost:8000. Una vez que tengamos creada nuestra aplicación en Mercado Libre debemos copiar App ID, Secret Key y asignarselos a CLIENT_ID (como número) y a CLIENT_SECRET (como string). 


### Librerias utilizadas

* [AngularJS] 
* [Twitter Bootstrap]

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [AngularJS]: <http://angularjs.org>
