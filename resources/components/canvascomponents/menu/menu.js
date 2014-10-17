angular.module('canvascomponentsMenu',['servoy']).directive('canvascomponentsMenu', function() {  
    return {
      restrict: 'E',
      controller: function($scope, $element, $attrs) {
    	 
      },
      templateUrl: 'canvascomponents/menu/menu.html',
	  replace: true
    };
  })