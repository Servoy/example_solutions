angular.module('canvascomponentsCollapseicon',['servoy']).directive('canvascomponentsCollapseicon', function() {  
    return {
      restrict: 'E',
      scope: {
        model: "=svyModel",
       	handlers: "=svyHandlers"
      },
      controller: function($scope, $element, $attrs) {
      },
      templateUrl: 'canvascomponents/collapseicon/collapseicon.html',
      replace: true
    };
  })