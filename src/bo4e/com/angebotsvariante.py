"""
Contains Angebotsvariante and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import TYPE_CHECKING, Optional

import pydantic

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

    #: Gibt den Status eines Angebotes an.
    angebotsstatus: Optional["Angebotsstatus"] = None

    #: Datum der Erstellung der Angebotsvariante
    erstellungsdatum: Optional[pydantic.AwareDatetime] = None

    #: Bis zu diesem Zeitpunkt gilt die Angebotsvariante
    bindefrist: Optional[pydantic.AwareDatetime] = None

    teile: Optional[list["Angebotsteil"]] = None
    """
    Angebotsteile werden im einfachsten Fall für eine Marktlokation oder Lieferstellenadresse erzeugt.
    Hier werden die Mengen und Gesamtkosten aller Angebotspositionen zusammengefasst.
    Eine Variante besteht mindestens aus einem Angebotsteil.
    """

    #: Aufsummierte Wirkarbeitsmenge aller Angebotsteile
    gesamtmenge: Optional["Menge"] = None
    # todo: write a validator for this: https://github.com/Hochfrequenz/BO4E-python/issues/320
    #: Aufsummierte Kosten aller Angebotsteile
    gesamtkosten: Optional["Betrag"] = None
