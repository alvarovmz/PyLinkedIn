# Copyright 2012 Alvaro Vila
# alvarovmz@gmail.com

# This file is part of PyLinkedIn.  

# PyLinkedIn is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyLinkedIn is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyLinkedIn.  If not, see <http://www.gnu.org/licenses/>.

from Requester import Requester
import LinkedInUser

class LinkedIn( object ):
    def __init__(   self, 
                    api_key=None, 
                    api_secret=None, 
                    oauth_token=None, 
                    oauth_token_secret=None):

        self.__requester = Requester( api_key, api_secret, oauth_token, oauth_token_secret)

    @property
    def rate_limiting( self ):
        return self.__requester.rate_limiting

    def get_user( self, login = None ):

        headers, data = self.__requester.requestAndCheck(
            "GET",
            'http://api.linkedin.com/v1/people/~',
            ['id','first-name'],
            None
        )

        return LinkedInUser.LinkedInUser( self.__requester, data, completed = True )

