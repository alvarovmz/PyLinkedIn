{% with template_name="LinkedInObject.AttributeValue.complex."|add:attribute.type.cardinality|add:".py" %}None if attributes[ "{{ attribute.name }}" ] is None else {% include template_name %}{% endwith %}
