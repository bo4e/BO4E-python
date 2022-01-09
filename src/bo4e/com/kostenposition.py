"""
Contains Kostenposition and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Optional

import attr
from marshmallow import fields

from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.menge import Menge, MengeSchema
from bo4e.com.preis import Preis, PreisSchema
from bo4e.validators import check_bis_is_later_than_von


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attr.s(auto_attribs=True, kw_only=True)
class Kostenposition(COM):
    """
    Diese Komponente wird zur Übertagung der Details zu einer Kostenposition verwendet.
    """

    # required attributes
    #: Ein Titel für die Zeile. Hier kann z.B. der Netzbetreiber eingetragen werden, wenn es sich um Netzkosten handelt.
    positionstitel: str = attr.ib(validator=attr.validators.instance_of(str))

    betrag_kostenposition: Betrag = attr.ib(validator=attr.validators.instance_of(Betrag))
    """Der errechnete Gesamtbetrag der Position als Ergebnis der Berechnung <Menge * Einzelpreis> oder
    <Einzelpreis / (Anzahl Tage Jahr) * zeitmenge>"""
    # todo: validate above calculation, see https://github.com/Hochfrequenz/BO4E-python/issues/282

    #: Bezeichnung für den Artikel für den die Kosten ermittelt wurden. Beispiel: Arbeitspreis HT
    artikelbezeichnung: str = attr.ib(validator=attr.validators.instance_of(str))

    #: Der Preis für eine Einheit. Beispiele: 5,8200 ct/kWh oder 55 €/Jahr.
    einzelpreis: Preis = attr.ib(validator=attr.validators.instance_of(Preis))

    # optional attributes
    #: inklusiver von-Zeitpunkt der Kostenzeitscheibe
    von: Optional[datetime] = attr.ib(
        default=None,
        validator=attr.validators.optional([attr.validators.instance_of(datetime), check_bis_is_later_than_von]),
    )
    #: exklusiver bis-Zeitpunkt der Kostenzeitscheibe
    bis: Optional[datetime] = attr.ib(
        default=None,
        validator=attr.validators.optional([attr.validators.instance_of(datetime), check_bis_is_later_than_von]),
    )

    #: Die Menge, die in die Kostenberechnung eingeflossen ist. Beispiel: 3.660 kWh
    menge: Optional[Menge] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Menge))
    )

    zeitmenge: Optional[Menge] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(Menge))
    )
    """
    Wenn es einen zeitbasierten Preis gibt (z.B. €/Jahr), dann ist hier die Menge angegeben mit der die Kosten berechnet
    wurden. Z.B. 138 Tage.
    """

    #: Detaillierung des Artikels (optional). Beispiel: 'Drehstromzähler'
    artikeldetail: Optional[str] = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(str))
    )

    def _get_inclusive_start(self) -> Optional[datetime]:
        return self.von

    def _get_exclusive_end(self) -> Optional[datetime]:
        return self.bis


class KostenpositionSchema(COMSchema):
    """
    Schema for de-/serialization of Kostenposition
    """

    class_name = Kostenposition
    # required attributes
    positionstitel = fields.Str()
    betrag_kostenposition = fields.Nested(BetragSchema)
    artikelbezeichnung = fields.Str()
    einzelpreis = fields.Nested(PreisSchema)

    # optional attributes
    von = fields.DateTime(allow_none=True)
    bis = fields.DateTime(allow_none=True)
    menge = fields.Nested(MengeSchema, allow_none=True)
    zeitmenge = fields.Nested(MengeSchema, allow_none=True)
    artikeldetail = fields.Str(allow_none=True)
