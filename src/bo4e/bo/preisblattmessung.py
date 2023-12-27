"""
Contains PreisblattMessung class and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated, Optional

from pydantic import Field

from ..bo.geraet import Geraet
from ..bo.zaehler import Zaehler
from ..enum.bilanzierungsmethode import Bilanzierungsmethode
from ..enum.dienstleistungstyp import Dienstleistungstyp
from ..enum.netzebene import Netzebene
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .preisblatt import Preisblatt

# pylint: disable=too-few-public-methods


@postprocess_docstring
class PreisblattMessung(Preisblatt):
    """
    Variante des Preisblattmodells zur Abbildung der Preise des Messstellenbetriebs und damit verbundener Leistungen

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattMessung.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattMessung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/PreisblattMessung.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.PREISBLATTMESSUNG
    # required attributes (additional to those of Preisblatt)
    #: Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode
    bilanzierungsmethode: Optional[Bilanzierungsmethode] = None
    #: Die Preise gelten für Messlokationen in der angebebenen Netzebene
    messebene: Optional[Netzebene] = None

    #: Der Preis betrifft den hier angegebenen Zähler, z.B. einen Drehstromzähler
    zaehler: Optional[Zaehler] = None

    #: Im Preis sind die hier angegebenen Dienstleistungen enthalten, z.B. Jährliche Ablesung
    inklusive_dienstleistungen: Optional[list[Dienstleistungstyp]] = None

    #: Im Preis sind die hier angegebenen Geräte mit enthalten, z.B. ein Wandler
    inklusive_geraete: Optional[list[Geraet]] = None
