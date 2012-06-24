You don't normaly create instances of any class but `LinkedIn`.
You obtain instances through calls to `get_` and `create_` methods.
Class `LinkedIn`
==============
* Constructed from user's login and password or OAuth token
* `get_user()`: `AuthenticatedUser`
* `get_user( login )`: `NamedUser`
* `get_organization( login )`: `Organization`
* `get_gist( id )`: `Gist`
* `get_gists()`: list of `Gist`
* `rate_limiting`: tuple of two integers: remaining and limit, as explained in [Rate Limiting](http://developer.linkedin.com/v3/#rate-limiting)

Class `Language`
================

Attributes
----------
* `id`: integer
* `language`: `LanguageDescription`

Class `LanguageDescription`
===========================

Attributes
----------
* `name`: string

Class `LinkedInUser`
====================

Attributes
----------
* `firstName`: string

Languages
---------
* `get_languages(

)`: list of `Language`
Skills
------
* `get_skills(

)`: list of `Skill`
Class `Skill`
=============

Attributes
----------
* `id`: integer
* `skill`: `SkillDescription`

Class `SkillDescription`
========================

Attributes
----------
* `name`: string
