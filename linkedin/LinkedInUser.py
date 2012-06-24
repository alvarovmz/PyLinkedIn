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
import PaginatedList

import Skill
import LinkedInUser
import Language

class LinkedInUser( LinkedInObject.BasicLinkedInObject ):
    @property
    def firstName( self ):
        return self._NoneIfNotSet( self._firstName )

    @property
    def headline( self ):
        return self._NoneIfNotSet( self._headline )

    @property
    def industry( self ):
        return self._NoneIfNotSet( self._industry )

    @property
    def lastName( self ):
        return self._NoneIfNotSet( self._lastName )

    @property
    def maidenName( self ):
        return self._NoneIfNotSet( self._maidenName )

    def get_connections( self):
        headers, data = self._requester.requestAndCheck(
            "GET",
            "http://api.linkedin.com/v1/people/~/connections" ,
            None,
            None
        )
        return PaginatedList.PaginatedList(
            LinkedInUser,
            self._requester,
            headers,
            data
        )

    def get_languages( self):
        headers, data = self._requester.requestAndCheck(
            "GET",
            "http://api.linkedin.com/v1/people/~/languages" ,
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Language.Language,
            self._requester,
            headers,
            data
        )

    def get_skills( self):
        headers, data = self._requester.requestAndCheck(
            "GET",
            "http://api.linkedin.com/v1/people/~/skills" ,
            None,
            None
        )
        return PaginatedList.PaginatedList(
            Skill.Skill,
            self._requester,
            headers,
            data
        )

    def _initAttributes( self ):
        self._firstName = LinkedInObject.NotSet
        self._headline = LinkedInObject.NotSet
        self._industry = LinkedInObject.NotSet
        self._lastName = LinkedInObject.NotSet
        self._maidenName = LinkedInObject.NotSet

    def _useAttributes( self, attributes ):
        if "firstName" in attributes: # pragma no branch
            assert attributes[ "firstName" ] is None or isinstance( attributes[ "firstName" ], ( str, unicode ) )\
, attributes[ "firstName" ]
            self._firstName = attributes[ "firstName" ]
        if "headline" in attributes: # pragma no branch
            assert attributes[ "headline" ] is None or isinstance( attributes[ "headline" ], ( str, unicode ) )\
, attributes[ "headline" ]
            self._headline = attributes[ "headline" ]
        if "industry" in attributes: # pragma no branch
            assert attributes[ "industry" ] is None or isinstance( attributes[ "industry" ], ( str, unicode ) )\
, attributes[ "industry" ]
            self._industry = attributes[ "industry" ]
        if "lastName" in attributes: # pragma no branch
            assert attributes[ "lastName" ] is None or isinstance( attributes[ "lastName" ], ( str, unicode ) )\
, attributes[ "lastName" ]
            self._lastName = attributes[ "lastName" ]
        if "maidenName" in attributes: # pragma no branch
            assert attributes[ "maidenName" ] is None or isinstance( attributes[ "maidenName" ], ( str, unicode ) )\
, attributes[ "maidenName" ]
            self._maidenName = attributes[ "maidenName" ]
