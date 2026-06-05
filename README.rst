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
.. _license: https://github.com/Hochfrequenz/BO4E-python/blob/main/LICENSE.rst

.. |code style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
.. _`code style`: https://github.com/psf/black

.. |PyPI pyversions| image:: https://img.shields.io/pypi/pyversions/bo4e.svg
.. _`PyPI pyversions`: https://pypi.python.org/pypi/bo4e/


🇩🇪 Dies ist eine BO4E Referenz-Implementierung in Python.
Gleichzeitig ist dieses Repository der Ort, um Fragen und Erweiterungen des BO4E-Standards zu diskutieren.

🇬🇧 This is a Python library that implements Business Objects for Energy `BO4E <https://www.bo4e.de/>`_.

Grundsätzliche Überlegungen
===========================

Pflichtfelder (nicht nullable Attributes)
-----------------------------------------
Der BO4E Standard soll (in Zukunft, Stand 2023-10-05) keine fachlichen Pflichtfelder mehr enthalten.
Die Entscheidung, was in welchen Fällen ein Pflichtfeld ist, obliegt den Anwendungen, die den Standard nutzen.
Entsprechend ist auch die Validierung der Pflichtfelder nicht Teil des BO4E Standards sondern anwendungsspezifisch.
Davon sind auch technische Pflichtfelder, namentlich `_typ` und `_version` nicht ausgenommen.
Ob sie anzugeben sind, entscheidet die Anwendung.
BO4E gibt sinnvolle Datenstrukturen vor, wie diese in der Praxis genutzt werden können und wollen wir aber nicht vorschreiben.

Verweise zwischen Objekten
-------------------------------
Viele Objekte verweisen aufeinander und sind miteinander verknüpft.
Dabei sind unsere Designentscheidungen:

* Alle Verweise sind optional.
* Verweise sind, wo sie naheliegend sind, im BO4E Standard vordefiniert (z.B. 1 Messlokation hat n Zähler).
* Aber wir haben nicht jede theoretisch denkbare Verweise implementiert (z.B. allein dass User Zähler unter Angabe einer Email-Adresse suchen können, heißt nicht, dass der Zähler eine optionale Eigenschaft `emailAdresse` haben muss.)
* Generell sollen Verweise zwischen zwei BOs bi-direktional sein, zwischen BOs und COMs aber nur unidirektional (z.B. soll jeder Zähler wissen zu welcher Messlokation er gehört aber eine Adresse muss nicht wissen, welchem Geschäftspartner, welcher Messlokation oder welcher Rechnung sie zugeordnet ist).
* COMs können zwar weitere COMs beinhalten, jedoch sollte dies nicht dafür genutzt werden von einem COM eines BOs auf das COM eines anderen BOs zu verweisen.
  Bsp.: Die Adresse in Ansprechpartner ist identisch zur Lokationsadresse in der Marktlokation. Dann sollen beide Adressen als vollständiges COM dargestellt werden, statt nur als Verweis von einer Adresse auf die andere.
* Oder anders formuliert: wir können aus einem BO oder einem COM auf ein anderes BO verweisen.

Dokumentation / Fragen und Anregungen zum BO4E Datenmodell
==========================================================
Die Dokumentation ist verfügbar unter `<https://bo4e.github.io/BO4E-python/>`_.
Die Doku wird erst seit Version `v202401.0.3 <https://bo4e.github.io/BO4E-python/v202401.0.3>`_ mittels
GitHub Pages gehosted.
Die früheren Versionen sind auf `read the docs <https://bo4e-python.readthedocs.io/en/latest/api/modules.html>`_
einsehbar.

Unter `/latest` findet sich die Dokumentation des aktuellen Stands des main-Branches. `/stable` zeigt immer auf die
letzte veröffentlichte Version (Release candidates ausgeschlossen).
Zusätzlich ist jede Version (inklusive Release candidates) unter `/v<version>` auffindbar.

Die Doku bietet eine Übersicht über alle Klassen und Attribute, die im BO4E Standard definiert sind. Außerdem
werden alle Beziehungen zwischen den Klassen durch Diagramme visualisiert. Die JSON-Schemas sind ebenfalls verlinkt.
Alternativ können die JSON-Schemas auch direkt von GitHub heruntergeladen werden: `<https://github.com/bo4e/BO4E-Schemas>`_.
Seit Version `v202401.1.1 <https://bo4e.github.io/BO4E-python/v202401.1.1>`_ gibt es zusätzlich eine
`Kompatibilitätsmatrix <https://bo4e.github.io/BO4E-python/v202401.1.1/changelog.html>`_,
die für jedes Objekt zeigt, zwischen welchen Versionen es einen "breaking change" gab.

Bei Fragen oder Anregungen, bitte `einfach ein Issue in diesem Repo aufmachen <https://github.com/Hochfrequenz/BO4E-python/issues/new?assignees=&labels=BO4E+Enhancement+Proposal&template=funktionale-anforderung-an-den-bo4e-standard.md&title=Ein+aussagekr%C3%A4ftiger+Titel%3A+Hunde-+und+Katzentarife+k%C3%B6nnen+nicht+abgebildet+werden>`_.

Code Beiträge
=============
Änderungsvorschläge (sowohl an das Datenmodell als auch an die Implementierung in Python) können direkt als Code in Form von Pull Requests eingereicht werden.
Details dazu finden sich im `Contribution Guide <https://bo4e.github.io/BO4E-python/latest/contributing_guide.html>`_.

Entwicklungs-Setup
==================
Die Entwicklungs-Abhängigkeiten sind in ``pyproject.toml`` unter ``[dependency-groups]`` (PEP 735) zentral gepflegt und über ``uv.lock`` gepinnt. ``uv`` (https://docs.astral.sh/uv/) wird als Paket-Manager verwendet, ``tox-uv`` integriert ihn in die bestehenden ``tox``-Umgebungen.

.. code-block:: shell

       # uv installieren (einmalig), siehe https://docs.astral.sh/uv/getting-started/installation/
       curl -LsSf https://astral.sh/uv/install.sh | sh

       # Repo klonen und volles Entwickler-Setup installieren
       git clone https://github.com/bo4e/BO4E-python.git
       cd BO4E-python
       uv sync --group dev

       # Einzelne tox-Umgebung ausführen (tox + tox-uv werden via uv installiert)
       uv run tox -e tests
       uv run tox -e linting
       uv run tox -e docs

Die verfügbaren Gruppen sind: ``tests``, ``coverage``, ``type_check``, ``linting``, ``formatting``, ``packaging``, ``json_schemas``, ``docs`` und ``dev`` (Sammel-Gruppe, enthält alle anderen plus ``pre-commit``).

Nutzung als Python Library
==========================
In Python kann diese Library als Paket installiert werden:

.. code-block::

       pip install bo4e


Andere nennenswerte BO4E Implementierungen
==========================================

* `C#/.NET <https://github.com/Hochfrequenz/BO4E-dotnet>`_
* `Golang <https://github.com/Hochfrequenz/go-bo4e/>`_
* `Kotlin <https://github.com/openEnWi/ktBO4E-lib>`_
* `TypeScript (handcrafted) <https://github.com/openEnWi/tsBO4E-lib>`_
* `TypeScript (autogenerated, inherently consistent with the .NET library) <https://github.com/Hochfrequenz/bo4e-dotnet-ts-models>`_
* `PHP <https://github.com/conuti-gmbh/bo4e-php/>`_ (und `Schemas <https://github.com/conuti-gmbh/bo4e-schema>`_)

.. _`BO4E website`: https://www.bo4e.de/dokumentation
