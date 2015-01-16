{
	"name": "servoycomponents-namepanel",
	"displayName": "Name panel",
	"version": 1,
	"definition": "servoycomponents/namepanel/namepanel.js",
	"model":
	{
		"bgcolor": "color",
	    "firstNameDataprovider": "dataprovider",
	    "firstNameTabsequence": {"type": "tabseq", "tags": { "scope": "design" }},
	    "lastNameDataprovider": "dataprovider",
	    "lastNameTabsequence": {"type": "tabseq", "tags": { "scope": "design" }},
		"buttontext": {"type":"string", "default":"button"},
		"buttonClass": { "type":"styleclass", "values":["btn","btn-default","btn-lg","btn-sm","btn-xs"]},
		"cssClasses" : { "type":"styleclass", "default":"table"},
		"tooltiptext": "string",
		"readOnly": "protected",
		"visible": "visible",
		"size" : {"type" :"dimension",  "default" : {"width":230, "height":120}}, 
	    "firstNameFormat": {"for":"firstNameDataprovider" , "type":"format"},
	    "testruntime": { "type": "string", "tags": { "scope":"runtime" }}
	},
	"handlers":
	{
	    "onAction": "function"
	}
}
