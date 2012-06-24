# Copyright 2012 Alvaro Vila
# alvarovmz@gmail.com

# This file is part of PyLinkedIn. http://vincent-jacques.net/PyLinkedIn

# PyLinkedIn is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyLinkedIn is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyLinkedIn.  If not, see <http://www.gnu.org/licenses/>.

import LinkedInObject

class PaginatedList:
    def __init__( self, contentClass, requester, headers, data ):
        self.__requester = requester
        self.__contentClass = contentClass
        self.__elements = []
        self.__appendData( headers, data )

    def __iter__( self ):
        for element in self.__elements:
            yield element
        while self.__nextUrl is not None:
            newElements = self.__fetchNextPage()
            for element in newElements:
                yield element

    class __Slice:
        def __init__( self, theList, theSlice ):
            self.__list = theList
            self.__start = theSlice.start or 0
            self.__stop = theSlice.stop
            self.__step = theSlice.step or 1

        def __iter__( self ):
            index = self.__start
            while not self.__finished( index ) :
                if self.__list._isBiggerThan( index ):
                    yield self.__list[ index ]
                    index += self.__step
                else:
                    return

        def __finished( self, index ):
            return self.__stop is not None and index >= self.__stop

    def __getitem__( self, index ):
        assert isinstance( index, ( int, slice ) )
        if isinstance( index, int ):
            self.__fetchToIndex( index )
            return self.__elements[ index ]
        else:
            return self.__Slice( self, index )

    def _isBiggerThan( self, index ):
        return len( self.__elements ) > index or self.__nextUrl is not None

    def __fetchToIndex( self, index ):
        while len( self.__elements ) <= index and self.__nextUrl is not None:
            self.__fetchNextPage()

    def __fetchNextPage( self ):
        headers, data = self.__requester.requestAndCheck( "GET", self.__nextUrl, None, None )
        return self.__appendData( headers, data )

    def __appendData( self, headers, data ):
        self.__nextUrl = None #TODO

        newElements = [
            self.__contentClass( self.__requester, element, completed = False )
            for element in data['values']
        ]
        self.__elements += newElements

        return newElements

