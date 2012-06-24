all( {% with template_name="LinkedInObject.IsInstance."|add:type.name|add:".py" %}{% include template_name with variable="element" only %}{% endwith %} for element in {{ variable }} )
