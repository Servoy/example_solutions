angular.module('canvascomponentsMenuitem',['servoy']).directive('canvascomponentsMenuitem', function() {  
    return {
      restrict: 'E',
      scope: {
        model: "=svyModel",
       	handlers: "=svyHandlers"
      },
      controller: function($scope, $element, $attrs) {
      },
      templateUrl: 'canvascomponents/menuitem/menuitem.html',
      replace: true
    };
  })