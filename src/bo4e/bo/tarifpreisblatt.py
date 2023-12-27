"""
Contains Tarifpreisblatt class and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Annotated, Optional

from pydantic import Field

from ..com.aufabschlag import AufAbschlag
from ..com.preisgarantie import Preisgarantie
from ..com.tarifberechnungsparameter import Tarifberechnungsparameter
from ..com.tarifeinschraenkung import Tarifeinschraenkung
from ..com.tarifpreisposition import Tarifpreisposition
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .tarifinfo import Tarifinfo

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module


@postprocess_docstring
class Tarifpreisblatt(Tarifinfo):
    """
    Tarifinformation mit Preisen, Aufschlägen und Berechnungssystematik

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Tarifpreisblatt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Tarifpreisblatt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Tarifpreisblatt.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.TARIFPREISBLATT
    # required attributes (additional to those of Tarifinfo)
    #: Gibt an, wann der Preis zuletzt angepasst wurde
    preisstand: Optional[datetime] = None
    #: Die festgelegten Preise, z.B. für Arbeitspreis, Grundpreis etc.
    tarifpreise: Optional[list[Tarifpreisposition]] = None
    #: Für die Berechnung der Kosten sind die hier abgebildeten Parameter heranzuziehen
    berechnungsparameter: Optional[Tarifberechnungsparameter] = None

    #: Die Bedingungen und Einschränkungen unter denen ein Tarif angewendet werden kann
    tarifeinschraenkung: Optional[Tarifeinschraenkung] = None
    #: Festlegung von Garantien für bestimmte Preisanteile
    preisgarantie: Optional[Preisgarantie] = None
    #: Auf- und Abschläge auf die Preise oder Kosten
    tarif_auf_abschlaege: Optional[list[AufAbschlag]] = None
