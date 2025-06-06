"""
Contains Angebotsvariante
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Annotated, Literal, Optional

import pydantic
from pydantic import Field

from ..enum.comtyp import ComTyp
from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.angebotsstatus import Angebotsstatus
    from .angebotsteil import Angebotsteil
    from .betrag import Betrag
    from .menge import Menge


@postprocess_docstring
class Angebotsvariante(COM):
    """
    Führt die verschiedenen Ausprägungen der Angebotsberechnung auf

    .. raw:: html

        <object data="../_static/images/bo4e/com/Angebotsvariante.svg" type="image/svg+xml"></object>

    .. HINT::
        `Angebotsvariante JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Angebotsvariante.json>`_

    """

    typ: Annotated[Literal[ComTyp.ANGEBOTSVARIANTE], Field(alias="_typ")] = ComTyp.ANGEBOTSVARIANTE

    angebotsstatus: Optional["Angebotsstatus"] = None
    """Gibt den Status eines Angebotes an."""

    erstellungsdatum: Optional[pydantic.AwareDatetime] = None
    """Datum der Erstellung der Angebotsvariante"""

    bindefrist: Optional[pydantic.AwareDatetime] = None
    """Bis zu diesem Zeitpunkt gilt die Angebotsvariante"""

    teile: Optional[list["Angebotsteil"]] = None
    """
    Angebotsteile werden im einfachsten Fall für eine Marktlokation oder Lieferstellenadresse erzeugt.
    Hier werden die Mengen und Gesamtkosten aller Angebotspositionen zusammengefasst.
    Eine Variante besteht mindestens aus einem Angebotsteil.
    """

    gesamtmenge: Optional["Menge"] = None
    """Aufsummierte Wirkarbeitsmenge aller Angebotsteile"""
    # todo: write a validator for this: https://github.com/Hochfrequenz/BO4E-python/issues/320
    gesamtkosten: Optional["Betrag"] = None
    """Aufsummierte Kosten aller Angebotsteile"""
