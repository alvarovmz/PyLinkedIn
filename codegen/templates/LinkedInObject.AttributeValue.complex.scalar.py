{% if attribute.type.name != class.name %}{{ attribute.type.name }}.{% endif %}{{ attribute.type.name }}( self._requester, attributes[ "{{ attribute.name }}" ], completed = False )
