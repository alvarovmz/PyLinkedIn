#!/usr/bin/env python

# Copyright 2012 Alvaro Vila
# alvarovmz@gmail.com

# This file is part of PyLinkedIn.  

# PyLinkedIn is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyLinkedIn is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyLinkedIn.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup
import textwrap

setup(
    name = "PyLinkedIn",
    version = "0.1",
    description = "Client for LinkedIn API",
    author = "Alvaro Vila",
    author_email = "alvarovmz@gmail.com",
    url = "http://github.com/alvarvmz/PyLinkedIn",
    long_description = textwrap.dedent( """\
        Tutorial
        ========

        First create a LinkedIn instance::

            from linkedin import LinkedIn

            g = LinkedIn( "api_key", "api_secret", "oauth_token", "oauth_token_secret" )

        Then play with your LinkedIn objects::

            for i in g.get_user().get_skills():
                print i.skill.name

        Reference documentation
        =======================

        See http://github.com/alvarovmz/PyLinkedIn""" ),
    packages = [
        "linkedin",
    ],
    package_data = {
        "linkedin": [ "../ReadMe.md", "../COPYING*", "../doc/*.md" ]
    },
    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
)
