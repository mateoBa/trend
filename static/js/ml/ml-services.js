var ml_service = angular.module('ml.services', ['ngResource']);

ml_service.service('mlService', ['$http', function($http) {

    this.login = function(){
        return $http({
            method: 'GET',
            url: '/login'
        });
    };

    this.getClientData = function(){
        return $http({
            method: 'GET',
            url: '/get_client_data/'
        });
    };

    this.getPublications = function(client_id) {
        return $http({
            method: 'GET',
            url: '/get_publications/',
            params: {client_id: client_id}
        });
    };

    this.getPublication = function(publication_id){
        return $http({
            method: 'GET',
            url: '/get_publication/',
            params: {publication_id: publication_id}
        });
    };

    this.savePublication = function (publication) {
        return $http({
            method: 'POST',
            url: '/save_publication/',
            data: publication
        })
    };

    this.logout = function () {
        return $http({
            method: 'GET',
            url: '/logout/'
        })
    }
}]);
