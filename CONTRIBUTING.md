# How to Contribute Code

This document describes how the BO4E Python implementation is written and what to watch out for.

## Technical Setup in your IDE

We're using tox.
Please follow the instructions in our [Python Template Repository](https://github.com/Hochfrequenz/python_template_repository#how-to-use-this-repository-on-your-machine).
Feel free to open an issue if you run into any kind of problems.

## Coding Style and Guidelines

### General Rules

- We use (and enforce in the CI):
  - black for formatting
  - pylint for linting
  - mypy for static type checking
  - pytest for unittests
  - Sphinx and Plantuml (and kroki web service) for documentation
- Technical Documentation is in English; For example: "Don't use the builtin validator here because …"
- But data model docstrings are in German; For example: "Ist das Ende nicht gesetzt, so ist der Zeitraum als offen zu verstehen."
- Docstrings should not be trivial/useless
  - Bad: "Energiemenge ist eine Klasse zur Abbildung von Energiemengen." ❌ (no shit sherlock)
  - Good: "Eine Energiemenge ordnet einer :class:`Marktlokation` oder :class:`Messlokation`, die über die `lokations_id` referenziert werden, einen oder mehrere Energieverbräuche zu." ✔
- Only sentences have a full stop at the end.
- We use `snake_case` internally but serialize as `camelCase` by overriding the `data_key` property of the schema fields.

### How to Define an ENUM?

All Enums inherit from `bo4e.enum.StrEnum`.
The latter is just a usual Enum with a `str` mixin (see [the official docs](https://docs.python.org/3/library/enum.html?highlight=strenum#others) for details).
This allows us to precisely define how an enum value will be serialized.
All enum values have UPPER_CASE names.

```python
# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class MyBo4eEnum(StrEnum):
    """
    Hier sollte ein deutscher Text stehen, der Sinn und Zweck des Enums beschreibt.
    """

    FOO = "FOO" #: FOO ist, wenn der Himmel blau ist
    BAR = "BAR"
    """
    Der Docstring für BAR kann auch hier drunter stehen, wenn er besonders lang ist und mehr sagen will,
    als dass BAR für die grüne Wiese steht. Denn manchmal braucht es mehr als hundert Zeichen.
    """
    EIGENSCHAFT_0815 = "0815" #: manchmal heißen eigenschaften anders (EIGENSCHAFT_0815) als sie serialisiert werden ("0815")
    # this typically happens for annoying enum values that contains "-" or start with digits
```

### How to Define `COM`s or `BO`s

All COMponents inherit from `bo4e.com.com.COM`.
All Business Objects inherit from `bo4e.bo.geschaeftsobjekt.Geschaeftsobjekt`.

For data validation and de/serialization we use [`pydantic`](https://pydantic-docs.helpmanual.io/).

```python
"""
Give the module a docstring to describe what it contains
"""

from pydantic import validator

from datetime import datetime
from typing import Optional, Dict, Any

from ..bo.geschaeftsobjekt import Geschaeftsobjekt
from ..com.menge import Menge
from ..enum.typ import BoTyp


# pylint: disable=too-few-public-methods
class MeinBo(Geschaeftsobjekt):
    """
    MeinBo ist ein ganz besonderes Business Objekt.
    Es kommt nur bei meinem Strom-Lieferanten zum Einsatz und beschreibt dort all die tollen Eigenschaften, die mein Verbrauchsverhalten hat.
    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.MEINBO


    #: Der Lieferbeginn beschreibt den Zeitpunkt ab dem (inklusiv) mich ein Versorger seinen Kunden nennen darf
    lieferbeginn: Optional[datetime] = None

    anzahl_freudenspruenge: Optional[int] = None
    """
    Anzahl Freudensprünge beschreibt, wie oft der CEO des Stromkonzerns in die Luft gesprungen ist, als ich den Vertrag unterschrieben habe.
    """

    #: Menge (Elektrische Energie oder Gas oder Wärme), die ich zum Lieferbeginn umsonst erhalte
    freimenge: Optional[Menge] = None

    # we can help you with anything you might be missing or unable to implement.
    # ToDo comments are just fine.
    # You don't need to be a perfect programmer to contribute to bo4e :)


```

### Unittests

Ideally provide unittests that show:

- that the BO/COM can be instantiated
  - with only the required attributes
  - with all attributes
- can be serialized and deserialized again
  - with only the required attributes
  - with all attributes

Therefore, copy one of the existing "roundtrip" tests, see f.e. `TestTarifeinschraenkung`.

## Pull Request

Open a Pull Request against the main/default branch of this repository.
We'd appreciate if you allowed maintainer edits.

## Release Workflow

- Check with tox all tests and linting: `tox`
- Check with tox if the packaging works fine: `tox -e test_packaging`
- Squash Merge all your changes you would like to have in the release into the main/default branch
- Check that all GitHub Actions for tests and linting do pass (should be automatically enforced for PRs against main)
- Go to the repositorys right sidebar and click on "[Draft a new release](https://github.com/Hochfrequenz/BO4E-python/releases/new)"
- Write in the _Tag version_ field and in the _Release title_ your new version, i.e. `v0.0.6`
- Add a description to the release (or just autogenerate the change log which will be fine for 95% of cases)
- Publish the release

There is a GitHub Action which gets triggered by a release event.
It will run all default tests with tox.
If they pass, it will take the tag title to replace the version information in the _setup.cfg_ file.
After checking the package with `twine check` it will finally upload the new package release.
