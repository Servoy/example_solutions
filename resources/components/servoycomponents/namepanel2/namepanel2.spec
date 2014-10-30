{
	"name": "servoycomponents-namepanel2",
	"displayName": "Name panel 2",
	"definition": "servoycomponents/namepanel2/namepanel2.js",
	"model":
	{
		"bgcolor": "color",
		"buttontext": {"type":"string", "default":"button"},
		"tooltiptext": "string",
		"complexmodel": {"type":"complextype", "droppable":true},
		"size" : {"type" :"dimension",  "default" : {"width":230, "height":120}}
	},
	"handlers":
	{
	    "onAction": "function"
	},
	"types": {
	  "complextype": {
	  		"firstNameDataprovider": { "type":"dataprovider"},
	  		"lastNameDataprovider": "tagstring"
	  }
	}
 }

