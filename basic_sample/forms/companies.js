
/**
 * Perform the element default action.
 *
 * @param {JSEvent} event the event that triggered the action
 *
 * @private
 *
 * @properties={typeid:24,uuid:"E62CD739-B0A7-40DD-8B84-57E4BFE4E6C7"}
 */
function onPreviousAction(event) 
{
	foundset.setSelectedIndex(foundset.getSelectedIndex()-1);
}

/**
 * Perform the element default action.
 *
 * @param {JSEvent} event the event that triggered the action
 *
 * @private
 *
 * @properties={typeid:24,uuid:"BB65631B-13B1-447F-9DD7-7E9C140469BA"}
 */
function onNextAction(event) {
	foundset.setSelectedIndex(foundset.getSelectedIndex()+1);
}
