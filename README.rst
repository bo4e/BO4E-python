=============
BO4E
=============
|PyPi|_
|license|_
|code style|_
|PyPI pyversions|_



.. |PyPi| image:: https://img.shields.io/pypi/v/bo4e.svg
.. _PyPi: https://img.shields.io/pypi/v/bo4e

.. |license| image:: https://img.shields.io/badge/License-MIT-blue.svg
.. _license: https://github.com/Hochfrequenz/BO4E-python/blob/master/LICENSE.rst

.. |code style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
.. _`code style`: https://github.com/psf/black

.. |PyPI pyversions| image:: https://img.shields.io/pypi/pyversions/bo4e.svg
.. _`PyPI pyversions`: https://pypi.python.org/pypi/bo4e/




Python Library that Implements `BO4E <https://www.bo4e.de/dokumentation>`_.
Requires Python >=3.8.

Other Noteworthy BO4E Implementations
=====================================

* `C#/.NET`_
* `Golang`_
* `Kotlin`_
* `TypeScript`_

Contributing
============
Contributions are welcome.
Feel free to open a Pull Request against the develop branch of this repository.
Please provide unit tests if you contribute logic beyond bare bare business object definitions.

To enhance this BO4E implementation and contribute to this project check out the `master branch`_, install `tox`_ and set the virtual environment created by the command

.. code-block:: Shell

   tox -e dev

The created venv should be located somewhere around .tox/dev/Scripts.

Release workflow
================
* Go to `BO4E-python`_ and click on "`Draft a new release`_" in the right sidebar
* Write in the *Tag version* field and in the *Release title* your new version, i.e. `v1.2.4`
* Add a describtion to the release or let it autogenerate
* Publish the release

There is a Github Action which gets triggered by a release event.
It will run all default tests with tox.
If they pass, it will take the tag title to replace the version information in the *setup.cfg* file.
After checking the package with `twine check` it will finally upload the new package release.

Hochfrequenz
============
`Hochfrequenz Unternehmensberatung GmbH`_ is a Grünwald (near Munich) based consulting company with offices in Berlin and Bremen.
According to `Kununu ratings`_ Hochfrequenz is among the most attractive employers within the German energy market.
Applications of talented developers are welcome at any time! Please consider visiting our `career page`_ that also contains job openings.


.. _`BO4E website`: https://www.bo4e.de/dokumentation
.. _`C#/.NET`: https://github.com/Hochfrequenz/BO4E-dotnet
.. _`Golang`: https://github.com/Hochfrequenz/go-bo4e/
.. _`Kotlin`: https://github.com/openEnWi/ktBO4E-lib
.. _`TypeScript`: https://github.com/openEnWi/tsBO4E-lib
.. _`Hochfrequenz Unternehmensberatung GmbH`: https://www.hochfrequenz.de
.. _`Kununu ratings`: https://www.kununu.com/de/hochfrequenz-unternehmensberatung1
.. _`career page`: https://www.hochfrequenz.de/karriere/stellenangebote/full-stack-entwickler/
.. _`master branch`: https://github.com/Hochfrequenz/BO4E-python/tree/master
.. _`tox`: https://pypi.org/project/tox/
.. _`BO4E-python`: https://github.com/Hochfrequenz/BO4E-python
.. _`Draft a new release`: https://github.com/Hochfrequenz/BO4E-python/releases/new
.. _`Retrieving package version at runtime`: https://pypi.org/project/setuptools-scm/
