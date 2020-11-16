=============
BO4E
=============
|PyPi|_
|license|_
|PyPI pyversions|_

.. |PyPi| image:: https://img.shields.io/pypi/v/bo4e.svg
.. _PyPi: https://img.shields.io/pypi/v/bo4e

.. |license| image:: https://img.shields.io/badge/License-MIT-blue.svg
.. _license: https://github.com/Hochfrequenz/BO4E-python/blob/master/LICENSE.rst

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
.. code-block:: shell

   tox -e dev 
   
The created venv should be located somewhere around .tox/dev/Scripts.

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
