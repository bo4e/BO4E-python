"""
Contains PreisblattNetnutzung class and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated, Optional

from pydantic import Field

from ..enum.bilanzierungsmethode import Bilanzierungsmethode
from ..enum.kundengruppe import Kundengruppe
from ..enum.netzebene import Netzebene
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .preisblatt import Preisblatt

# pylint: disable=too-few-public-methods


@postprocess_docstring
class PreisblattNetznutzung(Preisblatt):
    """
    Die Variante des Preisblattmodells zur Abbildung der Netznutzungspreise

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattNetznutzung.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattNetznutzung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/PreisblattNetznutzung.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.PREISBLATTNETZNUTZUNG
    # required attributes (additional to those of Preisblatt)
    #: Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode
    bilanzierungsmethode: Optional[Bilanzierungsmethode] = None
    #: Die Preise gelten für Marktlokationen in der angebebenen Netzebene
    netzebene: Optional[Netzebene] = None
    kundengruppe: Optional[Kundengruppe] = None

    # there are no optional attributes (additionally to those of Preisblatt)
