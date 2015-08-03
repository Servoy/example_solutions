{

	"name": "servoycomponents-configBasedFoundsetComponentSample",
	"version": 1,
	"displayName": "Foundset Config Based Sample Component",
	"definition": "servoycomponents/configBasedFoundsetComponent/configBasedFoundsetComponent.js",
	"libraries": 
	[
		
	],

	"model": 
	{
        "borderType" : { "type":"border" }, 
		"myfoundset": { "type": "foundset", "pushToServer": "allow" },
		"myconfiguration": { "type": "myConfig", "droppable": false },
		"notusedbutdroppableconfiguration": { "type": "myConfig", "droppable": true },
		"notusednotdroppableconfiguration": { "type": "myConfig", "droppable": false, "default": "{ 'ageBoundary' : 12345 }" },
		"notusedObjarray":  { "type":"columnNotUsed[]", "droppable": true },
		"notusedSimplearray" : "dataprovider[]"
	},

	"types": 
	{
		"myConfig": 
		{
			"mydataprovider": {	"type": "dataprovider",	"forFoundset": "myfoundset" },
			"mytagstring": { "type": "tagstring", "forFoundset": "myfoundset" },

			"toeditdataprovider": {	"type": "dataprovider",	"forFoundset": "myfoundset" },
			"statictagstring": { "type": "tagstring", "forFoundset": "myfoundset" },

			"format": "string",
			"ageBoundary": "int"
		},
		"columnNotUsed": 
		{
			"dataprovider": {	"type": "dataprovider",	"forFoundset": "myfoundset" },
			"format" : {"for":["valuelist","dataprovider"] , "type" :"format"}, 
			"headerText": {"type" :"string", "default" : "header"},
			"styleClass" : { "type" :"styleclass", "tags": { "scope" :"design" }},
			"nestedObject" : "myConfig",
			"nestedObjectArray" : "myConfig[]",
			"nestedSimplePropArray" : "int[]",
			"nestedDPArray" : "dataprovider[]",
			"valuelist" : { "type" : "valuelist", "tags": { "scope" :"design" }, "for": "dataprovider"} 
		}
		
	},

	"handlers": 
	{
		
	}
	
}