# Copyright 2012 Alvaro Vila
# alvarovmz@gmail.com

# This file is part of PyLinkedIn.  

# PyLinkedIn is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyLinkedIn is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyLinkedIn.  If not, see <http://www.gnu.org/licenses/>.

import httplib
import base64
import urllib
import oauth2 as oauth
import httplib2

try:
    import json
except ImportError: #pragma no cover: only for Python 2.5
    import simplejson as json #pragma no cover

import LinkedInException

class Requester:
    def __init__( self, api_key, api_secret, oauth_token, oauth_token_secret):
        # self.__authorizationHeader = "Basic " + base64.b64encode( login + ":" + password ).replace( '\n', '' )
        self.api_key = api_key
        self.api_secret = api_secret
        self.oauth_token = oauth_token
        self.oauth_secret = oauth_token_secret

        # Authentication URLs
        self.request_token_url = 'https://api.linkedin.com/uas/oauth/requestToken'
        self.access_token_url = 'https://api.linkedin.com/uas/oauth/accessToken'
        self.authorize_url = 'https://api.linkedin.com/uas/oauth/authorize'

        # If there's headers, set them. If not, lets
        self.headers = {}

        # ALL requests will be json. Enforcing it here...
        self.headers.update({'x-li-format': 'json',
                             'Content-Type': 'application/json'})

        self.consumer = None
        self.token = None

        client_args = {}

        # See if they're authenticating for the first or if they already have some tokens.
        if self.api_key is not None and self.api_secret is not None:
            self.consumer = oauth.Consumer(key=self.api_key, secret=self.api_secret)

        if self.oauth_token is not None and self.oauth_secret is not None:
            self.token = oauth.Token(key=oauth_token, secret=oauth_token_secret)

        if self.consumer is not None and self.token is not None:
            # Authenticated
            self.client = oauth.Client(self.consumer, self.token, **client_args)
        elif self.consumer is not None:
            # Authenticating
            self.client = oauth.Client(self.consumer, **client_args)
        else:
            # Unauthenticated requests (for LinkedIn calls available to public)
            self.client = httplib2.Http(**client_args)


    def requestAndCheck( self, verb, url, parameters, input ):
        status, headers, output = self.requestRaw( verb, url, parameters, input )
        if status >= 400:
            raise LinkedInException.LinkedInException( status, output )
        return headers, output

    def requestRaw( self, verb, url, parameters, input ):
        assert verb in [ "HEAD", "GET", "POST", "PATCH", "PUT", "DELETE" ]

        headers = dict()

        resp, content = self.client.request(self.__completeUrl( url, parameters ), verb, body=json.dumps(parameters), headers=self.headers)

        status = resp.status
        headers = resp
        output = self.__structuredFromJson( content )

        if "x-ratelimit-remaining" in headers and "x-ratelimit-limit" in headers:
            self.rate_limiting = ( int( headers[ "x-ratelimit-remaining" ] ), int( headers[ "x-ratelimit-limit" ] ) )

        return status, headers, output

    def __completeUrl( self, url, parameters ):
        if parameters is None or len( parameters ) == 0:
            return url
        else:
            return url + ":(%s)"% ",".join( parameters )

    def __structuredFromJson( self, data ):
        if len( data ) == 0:
            return None
        else:
            return json.loads( data )
