# Copyright 2012 Alvaro Vila
# alvarovmz@gmail.com
##########
# This file is part of PyLinkedIn.  
##########
# PyLinkedIn is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
##########
# PyLinkedIn is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.
##########
# You should have received a copy of the GNU Lesser General Public License along with PyLinkedIn.  If not, see <http://www.gnu.org/licenses/>.
##########

{% if class.needsUrllib %}
import urllib
{% endif %}
{% if class.needsDatetime %}
import datetime
{% endif %}
{% if class.needsUrllib or class.needsDatetime %}
##########
{% endif %}

import LinkedInObject
{% if class.needsPaginatedList %}
import PaginatedList
{% endif %}

{% if class.dependencies %}
##########
    {% for dependency in class.dependencies %}
import {{ dependency }}
    {% endfor %}
{% endif %}

{% if class.isCompletable %}
class {{ class.name }}( LinkedInObject.LinkedInObject ):
{% else %}
class {{ class.name }}( LinkedInObject.BasicLinkedInObject ):
{% endif %}

{% include "LinkedInObject.PublicAttributes.py" %}

{% include "LinkedInObject.PublicMethods.py" %}

{% include "LinkedInObject.Implementation.py" %}
