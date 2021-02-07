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




Python Library that Implements the `BO4E Standard`_.
Requires Python >=3.8. See also our `DOTNET implementation`_.

Contributing
============
Contributions are welcome.
Feel free to open a Pull Request against the develop branch of this repository.
Please provide unit tests if you contribute logic beyond bare bare business object definitions.

To enhance this BO4E implementation and contribute to this project check out the `develop branch`_, install `tox`_ and set the virtual environment created by the command

.. code-block:: Shell

   tox -e dev 
   
The created venv should be located somewhere around .tox/dev/Scripts.

Versioning
==========
To track the versions of this python package we use `setuptools-scm <https://pypi.org/project/setuptools-scm/>`_.
There are different kind of ways to achieve the version tracking. We will use the `pyproject.toml` usage.

To get the current version run in your working directory:

.. code-block:: Python

   python setup.py --version

At the moment it is not possible to get the version number at runtime.
To achieve this, we have to implement `Retrieving package version at runtime`_.

Release workflow
================
* Check with tox all tests and lintings: `tox`
* Check with tox if the packaging works fine: `tox -e test_packaging`
* Merge all your changes you would like to have in the release into the master branch (`open new PR develop→master`_)
* Check that all Github actions for tests and linting do pass (should be automatically enforced for PRs against master) 
* Go to `BO4E-python`_ and click on "`Draft a new release`_" in the right sidebar
* Write in the *Tag version* field and in the *Release title* your new version, i.e. `v0.0.6`
* Add a describtion to the release
* Publish the release

There is a github action which gets triggered by a release event.
It will run all default tests with tox. If they pass, it will take the tag title to replace the version information in the *setup.cfg* file.
After checking the package with `twine check` it will finally upload the new package release.

Hochfrequenz
============
`Hochfrequenz Unternehmensberatung GmbH`_ is a Grünwald (near Munich) based consulting company with offices in Berlin and Bremen.
According to `Kununu ratings`_ Hochfrequenz is among the most attractive employers within the German energy market.
Applications of talented developers are welcome at any time! Please consider visiting our `career page`_ that also contains job openings.


.. _`BO4E Standard`: https://www.bo4e.de/dokumentation
.. _`DOTNET implementation`: https://github.com/Hochfrequenz/BO4E-dotnet
.. _`Hochfrequenz Unternehmensberatung GmbH`: https://www.hochfrequenz.de
.. _`Kununu ratings`: https://www.kununu.com/de/hochfrequenz-unternehmensberatung1
.. _`career page`: https://www.hochfrequenz.de/karriere/stellenangebote/full-stack-entwickler/
.. _`develop branch`: https://github.com/Hochfrequenz/BO4E-python/tree/develop
.. _`tox`: https://pypi.org/project/tox/
.. _`BO4E-python`: https://github.com/Hochfrequenz/BO4E-python
.. _`open new PR develop→master`: https://github.com/Hochfrequenz/BO4E-python/compare/master...develop
.. _`Draft a new release`: https://github.com/Hochfrequenz/BO4E-python/releases/new
.. _`Retrieving package version at runtime`: https://pypi.org/project/setuptools-scm/
