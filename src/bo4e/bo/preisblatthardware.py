"""
Contains PreisblattHardware class and corresponding marshmallow schema for de-/serialization
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
    from ..enum.netzebene import Netzebene


# pylint: disable=too-few-public-methods


@postprocess_docstring
class PreisblattHardware(Preisblatt):
    """
    Variante des Preisblattmodells zur Abbildung der Preise für zusätzliche Hardware

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattHardware.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattHardware JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/PreisblattHardware.json>`_

    """

    typ: Annotated[Literal[Typ.PREISBLATTHARDWARE], Field(alias="_typ")] = (
        Typ.PREISBLATTHARDWARE  # type: ignore[assignment]
    )
    # required attributes (additional to those of Preisblatt)
    bilanzierungsmethode: Optional["Bilanzierungsmethode"] = None
    """Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode"""
    messebene: Optional["Netzebene"] = None
    """Die Preise gelten für Messlokationen in der angebebenen Netzebene"""

    basisgeraet: Optional["Geraet"] = None
    """Der Preis betriftt das hier angegebene Gerät, z.B. ein Tarifschaltgerät"""

    inklusive_dienstleistungen: Optional[list["Dienstleistungstyp"]] = None
    """Im Preis sind die hier angegebenen Dienstleistungen enthalten, z.B. Jährliche Ablesung"""

    inklusive_geraete: Optional[list["Geraet"]] = None
    """Im Preis sind die hier angegebenen Geräte mit enthalten, z.B. ein Wandler"""
