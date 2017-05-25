var ml_controller = angular.module('ml.controllers', []);

ml_controller.controller('mainCtrl', ['$scope', '$window' , 'mlService',
                                            function ($scope, $window, mlService) {
    $scope.login = function(){
        mlService.login().then(
            function(res){
                $window.location.href = res.data.url;
            },
            function(res){}
        );
    };
    $scope.logout = function(){
        mlService.logout().then(
            function (res) {
                $window.location.href = '/#!/main';
            },
            function (res) {
            }
        )
    };
    $scope.currentPath = $window.location.href;
}]);

ml_controller.controller('publicationCtrl', ['$scope', '$window' , 'mlService',
                                                    function($scope, $window, mlService) {
    $scope.publications = [];
    mlService.getClientData().then(
        function(res) {
            $scope.client = res.data;
            mlService.getPublications(res.data.id).then(
                function(res) {
                    $scope.publications = res.data.results;
                }, function(res){$scope.error = res.data.error});
        },
        function(res){
            $scope.error = res.data.error;
            $scope.error_description = res.data.error_description;
        }
    );
    $scope.publication = {};
    $scope.get_publication_detail = function(publication_id) {
        mlService.getPublication(publication_id).then(
            function (res) {
                $scope.publication = res.data;
            }, function (res) {alert('Error obteniendo detalles de publicación '+ publication_id)}
        )
    }
}]);

ml_controller.controller('createPubCtrl', ['$scope', '$window' , 'mlService',
                                            function ($scope, $window, mlService) {
    $scope.publication = {};
    $scope.save = function(publication){
        var pictures = [{source: publication.image1}];
        if (publication.image2){ pictures.push({source: publication.image2}) }
        var data_to_save = {title: publication.title, description: publication.description,
                            price: publication.price, currency_id: 'ARS', condition: 'new',
                            available_quantity: publication.stock, pictures: pictures, category_id: 'MLA352543', listing_type_id: 'bronze'};
        mlService.savePublication(data_to_save).then(
            function(res){
                console.log(res);
                console.log(res.data);
                console.log(res.data.status);
                if (res.data.status === 'active') {
                    alert('Se creó correctamente la reserva');
                    $window.location.href = '/#!/publications';
                }else{
                   alert('Error: status_code ' + res.data.status + '. '+res.data.error)
                }

            },
            function (res) {}
        );
    }
}]);
