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
		"myfoundset": { "type": "foundset" },
		"myconfiguration": { "type": "myConfig", "droppable": false }
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
		}
	},

	"handlers": 
	{
		
	}
	
}