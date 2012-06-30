PyLinkedin
==========

This is a Python library to access the [LinkedIn API](https://developer.linkedin.com/rest).

With it, you can manage your [LinkedIn](http://linkedin.com) resources (user profiles, companies, etc.) from Python scripts.

Should you have any question, or if you find a bug, or if there is something you can do with the API but not with PyLinkedIn, please [open an issue](https://github.com/alvarovmz/PyLinkedIn/issues).


Download and install
====================

Clone it on Github: [PyLinkedIn](http://github.com/alvarovmz/PyLinkedIn).

    git clone https://github.com/alvarovmz/PyLinkedIn.git

Or install it from the [Python Package Index](http://pypi.python.org/pypi/PyLinkedIn)

    pip install PyLinkedIn


Tutorial
========

First create a Linkedin instance:

    from linkedin import LinkedIn

Create a LinkedIn instance with:

    l = LinkedIn(api_key, api_secret, oauth_token, oauth_token_secret )


Licensing
=========

PyLinkedIn is distributed under the GNU Lesser General Public Licence.
See files COPYING and COPYING.LESSER, as requested by [GNU](http://www.gnu.org/licenses/gpl-howto.html).


History
=======

Version 0.1 (June 27th, 2012)
---------------------------

* User details:
    * Basic attributes
    * Skills
    * Languages
    * Connections
    * Certifications


Mentions
========
Original project from Vincent Jacques: [PyGithub](https://github.com/jacquev6/PyGithub)

Michael Helmick: [Linkedin API client](https://github.com/michaelhelmick/linkedin)
