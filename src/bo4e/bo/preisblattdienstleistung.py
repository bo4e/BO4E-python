"""
Contains PreisblattDienstleistung class and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .preisblatt import Preisblatt

if TYPE_CHECKING:
    from ..bo.geraet import Geraet
    from ..enum.bilanzierungsmethode import Bilanzierungsmethode
    from ..enum.dienstleistungstyp import Dienstleistungstyp


# pylint: disable=too-few-public-methods


@postprocess_docstring
class PreisblattDienstleistung(Preisblatt):
    """
    Variante des Preisblattmodells zur Abbildung der Preise für wahlfreie Dienstleistungen

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattDienstleistung.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattDienstleistung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/PreisblattDienstleistung.json>`_

    """

    typ: Annotated[Literal[Typ.PREISBLATTDIENSTLEISTUNG], Field(alias="_typ")] = (
        Typ.PREISBLATTDIENSTLEISTUNG  # type: ignore[assignment]
    )
    # required attributes (additional to those of Preisblatt)
    bilanzierungsmethode: Optional["Bilanzierungsmethode"] = None
    """Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode"""
    basisdienstleistung: Optional["Dienstleistungstyp"] = None
    """Dienstleistung, für die der Preis abgebildet wird, z.B. Sperrung/Entsperrung"""

    geraetedetails: Optional["Geraet"] = None
    """Hier kann der Preis auf bestimmte Geräte eingegrenzt werden. Z.B. auf die Zählergröße"""

    inklusive_dienstleistungen: Optional[list["Dienstleistungstyp"]] = None
    """Weitere Dienstleistungen, die im Preis enthalten sind"""
