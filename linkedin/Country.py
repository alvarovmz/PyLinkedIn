# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

# Copyright 2012 Alvaro Vila
# alvarovmz@gmail.com

# This file is part of PyLinkedIn.

# PyLinkedIn is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyLinkedIn is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyLinkedIn.  If not, see <http://www.gnu.org/licenses/>.

import LinkedInObject

class Country( LinkedInObject.BasicLinkedInObject ):
    @property
    def code( self ):
        return self._NoneIfNotSet( self._code )

    def _initAttributes( self ):
        self._code = LinkedInObject.NotSet

    def _useAttributes( self, attributes ):
        if "code" in attributes: # pragma no branch
            assert attributes[ "code" ] is None or isinstance( attributes[ "code" ], ( str, unicode ) )\
, attributes[ "code" ]
            self._code = attributes[ "code" ]
