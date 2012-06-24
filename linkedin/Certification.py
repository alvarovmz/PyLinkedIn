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

class Certification( LinkedInObject.BasicLinkedInObject ):
    @property
    def id( self ):
        return self._NoneIfNotSet( self._id )

    @property
    def name( self ):
        return self._NoneIfNotSet( self._name )

    def _initAttributes( self ):
        self._id = LinkedInObject.NotSet
        self._name = LinkedInObject.NotSet

    def _useAttributes( self, attributes ):
        if "id" in attributes: # pragma no branch
            assert attributes[ "id" ] is None or isinstance( attributes[ "id" ], int )\
, attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "name" in attributes: # pragma no branch
            assert attributes[ "name" ] is None or isinstance( attributes[ "name" ], ( str, unicode ) )\
, attributes[ "name" ]
            self._name = attributes[ "name" ]
