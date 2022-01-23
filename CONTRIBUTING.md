# How to Contribute Code
This document describes how the BO4E Python implementation is written and what to watch out for.

## Technical Setup in your IDE
We're using tox.
Please follow the instructions in our [Python Template Repository](https://github.com/Hochfrequenz/python_template_repository#how-to-use-this-repository-on-your-machine). 
Feel free to open an issue if you run into any kind of problems.

## Coding Style and Guidelines

### General Rules
* We use (and enforce in the CI):
  * black for formatting
  * pylint for linting
  * mypy for static type checking
  * pytest for unittests
  * Sphinx for documentation
* Technical Documentation is in English; For example: "Don't use the builtin validator here because ..."
* But data model docstrings are in German; For example: "Ist das Ende nicht gesetzt, so ist der Zeitraum als offen zuverstehen."
* Docstrings should not be trivial/useless
  * Bad: "Energiemenge ist eine Klasse zur Abbildung von Energiemengen." ❌ (no shit sherlock)
  * Good: "Eine Energiemenge ordnet einer :class:`Marktlokation` oder :class:`Messlokation`, die über die `lokations_id` referenziert werden, einen oder mehrere Energieverbräuche zu." ✔
* Only sentences have a fullstop at the end.
* we use `snake_case` internally but serialize as `camelCase` by overriding the `data_key` property of the schema fields

### How to create an ENUM
All Enums inherit from `StrEnum`.
It's is just a usual Enum with a `str` mixin (see [the official docs](see https://docs.python.org/3/library/enum.html?highlight=strenum#others) for details).
This allows us to precisly define how an enum value will be serialized.

```python
# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


class MyBo4eEnum(StrEnum):
    """
    Ein deutscher Text, der Sinn und Zweck des Enums beschreibt.
    """

    FOO = "FOO" #: FOO ist, wenn der Himmel blau ist
    BAR = "BAR"
    """
    Der Docstring für BAR kann auch hier drunter stehen, wenn er besonders lang ist und mehr sagen will,
    als dass BAR für die grüne Wiese steht. Denn manchmal braucht es mehr als hundert Zeichen.
    """
    EIGENSCHAFT_0815 = "0815" #: manchmal heißen eigenschaften anders als sie serialisiert werden.
    # this typically happens for annoying enum values that contains "-" or start with digits
 ```   
