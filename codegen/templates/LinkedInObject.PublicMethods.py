{% for method in class.methods|dictsort:"name" %}
    def {{ method.name|join:"_" }}( {% include "LinkedInObject.Parameters.py" with function=method only %} ):
        {% include "LinkedInObject.MethodBody.CheckArguments.py" %}
        {% include "LinkedInObject.MethodBody.DoRequest.py" %}
        {% include "LinkedInObject.MethodBody.CheckResult.py" %}
        {% include "LinkedInObject.MethodBody.UseResult.py" %}
{% endfor %}
