
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
            when('/login', {
                templateUrl: '/static/js/ml/templates/login.html',
                controller: 'controlSessionCtrl'
            }).
            when('/publications_list', {
                templateUrl: '/static/js/ml/templates/publications.html',
                controller: 'publicationCtrl'
            }).
            when('/create_publication', {
                templateUrl: '/static/js/ml/templates/create_publication.html',
                controller: 'publicationCtrl'
            }).
            when('/publication_detail/:publicationId', {
                templateUrl: '/static/js/ml/templates/publication_detail.html',
                controller: 'publicationCtrl'
            }).
            otherwise({
                templateUrl: '/static/js/app/contacts/404.html',
                controller: 'controlSessionCtrl'
            });
}]);


application.config(['$resourceProvider',
                    function($resourceProvider) {
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);