angular.module('servoycomponentsConfigBasedFoundsetComponentSample', ['servoy']).directive('servoycomponentsConfigbasedfoundsetcomponentsample', function($timeout) {
		return {
			restrict: 'E',
			transclude: true,
			scope: {
				model: "=svyModel",
				handlers: "=svyHandlers",
			},
			link: function($scope, $element, $attrs) {

				$scope.$watch('model.myfoundset.serverSize', function(newValue) {
						var wanted = Math.min(newValue, 10);
						if (wanted > $scope.model.myfoundset.viewPort.size) $scope.model.myfoundset.loadRecordsAsync(0, wanted);
					});
			},
			templateUrl: 'servoycomponents/configBasedFoundsetComponent/configBasedFoundsetComponent.html',
			replace: true
		};
	});