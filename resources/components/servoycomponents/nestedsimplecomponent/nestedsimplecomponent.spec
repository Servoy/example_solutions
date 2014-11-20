{
	"name": "servoycomponents-nestedsimplecomponent",
	"displayName": "Nested Simple Component",
	"version": 1,
	"definition": "servoycomponents/nestedsimplecomponent/nestedsimplecomponent.js",
	"model":
	{
		"titleText": {"type":"string", "default":"This is just a simple 2 child container with a title and border"},
        "borderType" : {"type":"border"}, 
	    "childComponent1": { "type": "component" },
	    "childComponent2": { "type": "component" }
	},
	"handlers":
	{
	    "onAction": "function"
	}
}
