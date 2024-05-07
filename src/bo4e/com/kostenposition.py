"""
Contains Kostenposition and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Optional

import pydantic

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:

    from .betrag import Betrag
    from .menge import Menge
    from .preis import Preis

# pylint: disable=too-few-public-methods, too-many-instance-attributes


@postprocess_docstring
class Kostenposition(COM):
    """
    Diese Komponente wird zur Übertagung der Details zu einer Kostenposition verwendet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Kostenposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Kostenposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Kostenposition.json>`_

    """

    #: Ein Titel für die Zeile. Hier kann z.B. der Netzbetreiber eingetragen werden, wenn es sich um Netzkosten handelt.
    positionstitel: Optional[str] = None

    betrag_kostenposition: Optional["Betrag"] = None
    """Der errechnete Gesamtbetrag der Position als Ergebnis der Berechnung <Menge * Einzelpreis> oder
    <Einzelpreis / (Anzahl Tage Jahr) * zeitmenge>"""
    # todo: validate above calculation, see https://github.com/Hochfrequenz/BO4E-python/issues/282

    #: Bezeichnung für den Artikel für den die Kosten ermittelt wurden. Beispiel: Arbeitspreis HT
    artikelbezeichnung: Optional[str] = None

    #: Der Preis für eine Einheit. Beispiele: 5,8200 ct/kWh oder 55 €/Jahr.
    einzelpreis: Optional["Preis"] = None

    #: inklusiver von-Zeitpunkt der Kostenzeitscheibe
    von: Optional[pydantic.AwareDatetime] = None
    #: exklusiver bis-Zeitpunkt der Kostenzeitscheibe
    bis: Optional[pydantic.AwareDatetime] = None

    #: Die Menge, die in die Kostenberechnung eingeflossen ist. Beispiel: 3.660 kWh
    menge: Optional["Menge"] = None

    zeitmenge: Optional["Menge"] = None
    """
    Wenn es einen zeitbasierten Preis gibt (z.B. €/Jahr), dann ist hier die Menge angegeben mit der die Kosten berechnet
    wurden. Z.B. 138 Tage.
    """

    #: Detaillierung des Artikels (optional). Beispiel: 'Drehstromzähler'
    artikeldetail: Optional[str] = None
