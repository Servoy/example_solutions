angular.module('canvascomponentsSimplehyperlink',['servoy']).directive('canvascomponentsSimplehyperlink', function() {  
    return {
      restrict: 'E',
      scope: {
        model: "=svyModel",
       	handlers: "=svyHandlers"
      },
      controller: function($scope, $element, $attrs) {
      },
      templateUrl: 'canvascomponents/simplehyperlink/simplehyperlink.html',
	  replace: true
    };
  })