angular.module('servoycomponentsNestedsimplecomponent',['servoy']).directive('servoycomponentsNestedsimplecomponent', function() {  
    return {
      restrict: 'E',
      scope: {
        model: "=svyModel"
      },
      controller: function($scope, $element, $attrs) {
      },
      templateUrl: 'servoycomponents/nestedsimplecomponent/nestedsimplecomponent.html'
    };
  })