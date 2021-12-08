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

Contributing
============
Contributions are welcome.
Feel free to open a Pull Request against the develop branch of this repository.
Please provide unit tests if you contribute logic beyond bare bare business object definitions.

To enhance this BO4E implementation and contribute to this project check out the `master branch`_, install `tox`_ and set the virtual environment created by the command

.. code-block:: Shell

   tox -e dev

The created venv should be located somewhere around .tox/dev/Scripts.

Regular Expression for Enumerations
-----------------------------------

If you want to add a new enumeration from the `BO4E website`_ then you can copy paste HTML table content and use the following regular expression pattern:

.. code-block:: Shell

    ^(?<wert>[A-Z\d_]+)\t(?<bedeutung>.+)$

In combination with this substitution:

.. code-block:: Shell

    "$wert": "$wert", #: $bedeutung

This substitution can directly used on the website `regex101`_.


Versioning
==========
| Short background information about versioning of python packages.
| At the moment (2021-02-10) there are `seven ways to define the version of your package <https://packaging.python.org/guides/single-sourcing-package-version/>`_.
| We use `setuptools-scm <https://pypi.org/project/setuptools-scm/>`_ for versioning so we can use the tags of git to define the version.
| The tool itself again has several ways how to configure it.
| We use the `pyproject.toml` file to configure setuptools-scm.
| There we tell the build-system with ``"setuptools_scm[toml]>=3.4"`` that we use setuptools_scm and the version must be at least ``3.4``.
| The ``[toml]`` section tells setuptools-scm that it finds all settings in our pyproject.toml file.
| ``[tool.setuptools_scm]`` in pyproject.toml enables version inference.
| In the setup.py we have to use the attribute ``use_scm_version=True``.

To create the version number itself, we stick to the default behavior of setuptools-scm.
It will take a look at three things:

1. latest tag (with a version number)
2. the distance to this tag (e.g. number of revisions since latest tag)
3. workdir state (e.g. uncommitted changes since latest tag)

and uses roughly the following logic to render the version:

no distance and clean:
    ``{tag}``
distance and clean:
    ``{next_version}.dev{distance}+{scm letter}{revision hash}``
no distance and not clean:
    ``{tag}+dYYYYMMDD``
distance and not clean:
    ``{next_version}.dev{distance}+{scm letter}{revision hash}.dYYYYMMDD``


The next version is calculated by adding 1 to the last numeric component of the tag.

To get the current version run in your working directory:

.. code-block:: Python

   python setup.py --version

At the moment it is not possible to get the version number at runtime.
To achieve this, we have to implement `Retrieving package version at runtime`_.

If you follow the instruction in the *release workflow*, you will get the version number which you define with the label name.

Release workflow
================
* Check with tox all tests and lintings: `tox`
* Check with tox if the packaging works fine: `tox -e test_packaging`
* Merge all your changes you would like to have in the release into the master branch
* Check that all Github actions for tests and linting do pass (should be automatically enforced for PRs against master)
* Go to `BO4E-python`_ and click on "`Draft a new release`_" in the right sidebar
* Write in the *Tag version* field and in the *Release title* your new version, i.e. `v0.0.6`
* Add a describtion to the release
* Publish the release

There is a Github Action which gets triggered by a release event.
It will run all default tests with tox. If they pass, it will take the tag title to replace the version information in the *setup.cfg* file.
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
.. _`Hochfrequenz Unternehmensberatung GmbH`: https://www.hochfrequenz.de
.. _`Kununu ratings`: https://www.kununu.com/de/hochfrequenz-unternehmensberatung1
.. _`career page`: https://www.hochfrequenz.de/karriere/stellenangebote/full-stack-entwickler/
.. _`master branch`: https://github.com/Hochfrequenz/BO4E-python/tree/master
.. _`tox`: https://pypi.org/project/tox/
.. _`BO4E-python`: https://github.com/Hochfrequenz/BO4E-python
.. _`Draft a new release`: https://github.com/Hochfrequenz/BO4E-python/releases/new
.. _`Retrieving package version at runtime`: https://pypi.org/project/setuptools-scm/
.. _`regex101`: https://regex101.com/r/JWeb51/2
