"""
Contains PreisblattKonzessionsabgabe class and corresponding marshmallow schema for de-/serialization
"""
from typing import Annotated, Optional

from pydantic import Field

from ..enum.kundengruppeka import KundengruppeKA
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .preisblatt import Preisblatt

# pylint: disable=too-few-public-methods


@postprocess_docstring
class PreisblattKonzessionsabgabe(Preisblatt):
    """
    Die Variante des Preisblattmodells zur Abbildung von allgemeinen Abgaben

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattKonzessionsabgabe.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattKonzessionsabgabe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/PreisblattKonzessionsabgabe.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.PREISBLATTKONZESSIONSABGABE
    # required attributes (additional to those of Preisblatt)
    #: Kundegruppe anhand derer die Höhe der Konzessionabgabe festgelegt ist
    kundengruppe_k_a: Optional[KundengruppeKA] = None

    # there are no optional attributes (additionally to those of Preisblatt)
