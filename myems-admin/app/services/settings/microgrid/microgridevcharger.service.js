'use strict';
app.factory('MicrogridEVChargerService', function($http) {
    return {
        getAllMicrogridEVChargers: function(headers, callback) {
            $http.get(getAPI()+'microgridevchargers', {headers})
            .then(function (response) {
                callback(response);
            }, function (response) {
                callback(response);
            });
        },
        getMicrogridEVChargersByMicrogridID: function(id, headers, callback) {
            $http.get(getAPI()+'microgrids/'+id+'/evchargers', {headers})
            .then(function (response) {
                callback(response);
            }, function (response) {
                callback(response);
            });
        },
        addMicrogridEVCharger: function(microgridevcharger, headers, callback) {
            $http.post(getAPI()+'/microgridevchargers',{data:microgridevcharger}, {headers})
            .then(function (response) {
                callback(response);
            }, function (response) {
                callback(response);
            });
        },
        editMicrogridEVCharger: function(microgridevcharger, headers, callback) {
            $http.put(getAPI()+'/microgridevchargers/'+microgridevcharger.id,{data:microgridevcharger}, {headers})
            .then(function (response) {
                callback(response);
            }, function (response) {
                callback(response);
            });
        },

        deleteMicrogridEVCharger: function(microgridevchargeryID, headers, callback) {
            $http.delete(getAPI()+'/microgridevchargers/'+microgridevchargeryID, {headers})
            .then(function (response) {
                callback(response);
            }, function (response) {
                callback(response);
            });
        },
    };
});
