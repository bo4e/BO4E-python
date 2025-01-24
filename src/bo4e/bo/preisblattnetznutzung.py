"""
Contains PreisblattNetnutzung class and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .preisblatt import Preisblatt

if TYPE_CHECKING:
    from ..enum.bilanzierungsmethode import Bilanzierungsmethode
    from ..enum.kundengruppe import Kundengruppe
    from ..enum.netzebene import Netzebene


# pylint: disable=too-few-public-methods


@postprocess_docstring
class PreisblattNetznutzung(Preisblatt):
    """
    Die Variante des Preisblattmodells zur Abbildung der Netznutzungspreise

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattNetznutzung.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattNetznutzung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/PreisblattNetznutzung.json>`_

    """

    typ: Annotated[Literal[Typ.PREISBLATTNETZNUTZUNG], Field(alias="_typ")] = (
        Typ.PREISBLATTNETZNUTZUNG  # type: ignore[assignment]
    )
    # required attributes (additional to those of Preisblatt)
    bilanzierungsmethode: Optional["Bilanzierungsmethode"] = None
    """Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode"""
    netzebene: Optional["Netzebene"] = None
    """Die Preise gelten für Marktlokationen in der angebebenen Netzebene"""
    kundengruppe: Optional["Kundengruppe"] = None

    # there are no optional attributes (additionally to those of Preisblatt)
