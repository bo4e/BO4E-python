"""
Contains Kostenposition and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Optional

# pylint: disable=too-few-public-methods, too-many-instance-attributes
from pydantic import field_validator
from pydantic_core.core_schema import ValidationInfo

from bo4e.com.betrag import Betrag
from bo4e.com.com import COM
from bo4e.com.menge import Menge
from bo4e.com.preis import Preis
from bo4e.validators import check_bis_is_later_than_von


class Kostenposition(COM):
    """
    Diese Komponente wird zur Übertagung der Details zu einer Kostenposition verwendet.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Kostenposition.svg" type="image/svg+xml"></object>

    .. HINT::
        `Kostenposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Kostenposition.json>`_

    """

    # required attributes
    #: Ein Titel für die Zeile. Hier kann z.B. der Netzbetreiber eingetragen werden, wenn es sich um Netzkosten handelt.
    positionstitel: str

    betrag_kostenposition: Betrag
    """Der errechnete Gesamtbetrag der Position als Ergebnis der Berechnung <Menge * Einzelpreis> oder
    <Einzelpreis / (Anzahl Tage Jahr) * zeitmenge>"""
    # todo: validate above calculation, see https://github.com/Hochfrequenz/BO4E-python/issues/282

    #: Bezeichnung für den Artikel für den die Kosten ermittelt wurden. Beispiel: Arbeitspreis HT
    artikelbezeichnung: str

    #: Der Preis für eine Einheit. Beispiele: 5,8200 ct/kWh oder 55 €/Jahr.
    einzelpreis: Preis

    # optional attributes
    #: inklusiver von-Zeitpunkt der Kostenzeitscheibe
    von: Optional[datetime] = None
    #: exklusiver bis-Zeitpunkt der Kostenzeitscheibe
    bis: Optional[datetime] = None
    _bis_check = field_validator("bis")(check_bis_is_later_than_von)

    #: Die Menge, die in die Kostenberechnung eingeflossen ist. Beispiel: 3.660 kWh
    menge: Optional[Menge] = None

    zeitmenge: Optional[Menge] = None
    """
    Wenn es einen zeitbasierten Preis gibt (z.B. €/Jahr), dann ist hier die Menge angegeben mit der die Kosten berechnet
    wurden. Z.B. 138 Tage.
    """

    #: Detaillierung des Artikels (optional). Beispiel: 'Drehstromzähler'
    artikeldetail: Optional[str] = None

    @staticmethod
    def _get_inclusive_start(values: ValidationInfo) -> Optional[datetime]:
        return values.data["von"]  # type:ignore[attr-defined]

    # @staticmethod
    # def _get_exclusive_end(values) -> Optional[datetime]:
    #     return values['bis']
