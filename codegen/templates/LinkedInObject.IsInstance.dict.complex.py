all( {% include "LinkedInObject.IsInstance.py" with variable="element" type=type.name|add:"."|add:type.name only %} for element in {{ variable }}.itervalues() )
