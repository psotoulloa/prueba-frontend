// Código para prueba
var  Tasks;
var resources = angular.module('resources', ['ngResource']);


Tasks = function($resource) {
    return $resource('http://apiprueba.dev.cl/api/tareas/:id', {}, {
        query: {
            method: 'GET',
            isArray: false
        },
        update : {
            method: 'PATCH',
            isArray: false
        }
    });
};

resources.factory('Tasks', ['$resource', Tasks]);

