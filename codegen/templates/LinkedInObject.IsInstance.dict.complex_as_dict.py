all( {% include "LinkedInObject.IsInstance.py" with variable="element" type="dict" only %} for element in {{ variable }}.itervalues() )
