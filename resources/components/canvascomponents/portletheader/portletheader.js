angular.module('canvascomponentsPortletheader',['servoy']).directive('canvascomponentsPortletheader', function() {  
    return {
      restrict: 'E',
      scope: {
          model: "=svyModel",
          handlers: "=svyHandlers"
        },
      controller: function($scope, $element, $attrs) {
    	 
      },
      templateUrl: 'canvascomponents/portletheader/portletheader.html',
	  replace: true
    };
  })