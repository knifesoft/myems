'use strict';

app.controller('CommandController', function(
	$scope,
	$rootScope,
	$window,
	$uibModal,
	$translate,
	CommandService,
	toaster,
	SweetAlert) {
	$scope.cur_user = JSON.parse($window.localStorage.getItem("myems_admin_ui_current_user"));
	$scope.getAllCommands = function() {
		let headers = { "User-UUID": $scope.cur_user.uuid, "Token": $scope.cur_user.token };
		CommandService.getAllCommands(headers, function (response) {
			if (angular.isDefined(response.status) && response.status === 200) {
				$scope.commands = response.data;
			} else {
				$scope.commands = [];
			}
		});
	};

	$scope.addCommand = function() {
		var modalInstance = $uibModal.open({
			templateUrl: 'views/settings/command/command.model.html',
			controller: 'ModalAddCommandCtrl',
			windowClass: "animated fadeIn",
		});
		modalInstance.result.then(function(command) {
			let headers = { "User-UUID": $scope.cur_user.uuid, "Token": $scope.cur_user.token };
			CommandService.addCommand(command, headers, function (response) {
				if (angular.isDefined(response.status) && response.status === 201) {
					toaster.pop({
						type: "success",
						title: $translate.instant("TOASTER.SUCCESS_TITLE"),
						body: $translate.instant("TOASTER.SUCCESS_ADD_BODY", {template: $translate.instant("SETTING.COMMAND")}),
						showCloseButton: true,
					});
					$scope.getAllCommands();
					$scope.$emit('handleEmitCommandChanged');
				} else {
					toaster.pop({
						type: "error",
						title: $translate.instant("TOASTER.ERROR_ADD_BODY", {template: $translate.instant("SETTING.COMMAND")}),
						body: $translate.instant(response.data.description),
						showCloseButton: true,
					});
				}
			});
		}, function() {

		});
		$rootScope.modalInstance = modalInstance;
	};

	$scope.editCommand=function(command){
		var modalInstance = $uibModal.open({
		    windowClass: "animated fadeIn",
		    templateUrl: 'views/settings/command/command.model.html',
		    controller: 'ModalEditCommandCtrl',
		    resolve: {
		        params:function(){
                    return {
                        command:angular.copy(command),
                        commands:angular.copy($scope.commands)
                    };
                }
		    }
		});

		modalInstance.result.then(function (modifiedCommand) {
			let headers = { "User-UUID": $scope.cur_user.uuid, "Token": $scope.cur_user.token };
	        CommandService.editCommand(modifiedCommand, headers, function (response){
	            if(angular.isDefined(response.status) && response.status === 200){
					toaster.pop({
						type: "success",
						title: $translate.instant("TOASTER.SUCCESS_TITLE"),
						body: $translate.instant("TOASTER.SUCCESS_UPDATE_BODY", {template: $translate.instant("SETTING.COMMAND")}),
						showCloseButton: true,
					});
			        $scope.getAllCommands();
					$scope.$emit('handleEmitCommandChanged');
		      } else {
					toaster.pop({
						type: "error",
						title: $translate.instant("TOASTER.ERROR_UPDATE_BODY", {template: $translate.instant("SETTING.COMMAND")}),
						body: $translate.instant(response.data.description),
						showCloseButton: true,
					});
				}
	        });
		}, function () {
	        //do nothing;
		});
		$rootScope.modalInstance = modalInstance;
	};

	$scope.deleteCommand=function(command){
		SweetAlert.swal({
		        title: $translate.instant("SWEET.TITLE"),
		        text: $translate.instant("SWEET.TEXT"),
		        type: "warning",
		        showCancelButton: true,
		        confirmButtonColor: "#DD6B55",
		        confirmButtonText: $translate.instant("SWEET.CONFIRM_BUTTON_TEXT"),
		        cancelButtonText: $translate.instant("SWEET.CANCEL_BUTTON_TEXT"),
		        closeOnConfirm: true,
		        closeOnCancel: true
			},
		    function (isConfirm) {
		        if (isConfirm) {
					let headers = { "User-UUID": $scope.cur_user.uuid, "Token": $scope.cur_user.token };
		            CommandService.deleteCommand(command, headers, function (response) {
		            	if (angular.isDefined(response.status) && response.status === 204) {
							toaster.pop({
								type: "success",
								title: $translate.instant("TOASTER.SUCCESS_TITLE"),
								body: $translate.instant("TOASTER.SUCCESS_DELETE_BODY", {template: $translate.instant("SETTING.COMMAND")}),
								showCloseButton: true,
							});
		            		$scope.getAllCommands();
							$scope.$emit('handleEmitCommandChanged');
		            	} else {
							toaster.pop({
			                  type: "error",
			                  title: $translate.instant("TOASTER.ERROR_DELETE_BODY", {template: $translate.instant("SETTING.COMMAND")}),
			                  body: $translate.instant(response.data.description),
			                  showCloseButton: true,
			              });
						}
		            });
		        }
		    });
	};
	$scope.sendCommand = function (command) {
		let headers = { "User-UUID": $scope.cur_user.uuid, "Token": $scope.cur_user.token };
        CommandService.sendCommand(command, headers, function (response) {
            if (angular.isDefined(response.status) && response.status === 200) {
                toaster.pop({
                    type: "success",
                    title: $translate.instant('TOASTER.SUCCESS_TITLE'),
                    body: $translate.instant('COMMAND.SEND_SUCCESS'),
                    showCloseButton: true,
                });
                $scope.getAllCommands();
            } else {
                toaster.pop({
                    type: "error",
                    title: $translate.instant(response.data.title),
                    body: $translate.instant(response.data.description),
                    showCloseButton: true,
                });
            }
        });
    };
	$scope.getAllCommands();

});

app.controller('ModalAddCommandCtrl', function ($scope, $uibModalInstance) {
    $scope.operation="SETTING.ADD_COMMAND";
    $scope.ok = function () {
        $uibModalInstance.close($scope.command);
    };

    $scope.cancel = function () {
        $uibModalInstance.dismiss('cancel');
    };
});

app.controller('ModalEditCommandCtrl', function ($scope, $uibModalInstance, params) {
    $scope.operation="SETTING.EDIT_COMMAND";
    $scope.command = params.command;
    $scope.commands=params.commands;

    $scope.ok = function() {
        $uibModalInstance.close($scope.command);
    };

    $scope.cancel = function() {
        $uibModalInstance.dismiss('cancel');
    };
});
