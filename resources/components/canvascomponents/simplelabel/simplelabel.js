angular.module('canvascomponentsSimplelabel',['servoy']).directive('canvascomponentsSimplelabel', function() {  
    return {
      restrict: 'E',
      scope: {
        model: "=svyModel",
       	handlers: "=svyHandlers",
		servoyApi: "=svyServoyapi"
      },
      controller: function($scope, $element, $attrs) {
      },
      templateUrl: 'canvascomponents/simplelabel/simplelabel.html',
	  replace: true
    };
  })