
var application = angular.module('ml-ngapp', [
    'ngRoute',
    'ngResource',

    //apps
    'ml'
]);

application.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

application.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/main', {
                templateUrl: '/static/js/ml/templates/main.html',
                controller: 'mainCtrl'
            }).
            when('/publications', {
                templateUrl: '/static/js/ml/templates/publications.html',
                controller: 'publicationCtrl'
            }).
            when('/create_publication', {
                templateUrl: '/static/js/ml/templates/create_publication.html',
                controller: 'createPubCtrl'
            }).
            when('/publication_detail/:publicationId', {
                templateUrl: '/static/js/ml/templates/publication_detail.html',
                controller: 'publicationCtrl'
            }).
            otherwise({
                redirectTo: '/main'
            });
}]);


application.config(['$resourceProvider',
                    function($resourceProvider) {
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);