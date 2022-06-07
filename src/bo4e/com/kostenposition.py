"""
Contains Kostenposition and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Optional

import attrs
from marshmallow import fields

from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.menge import Menge, MengeSchema
from bo4e.com.preis import Preis, PreisSchema
from bo4e.validators import check_bis_is_later_than_von


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attrs.define(auto_attribs=True, kw_only=True)
class Kostenposition(COM):
    """
    Diese Komponente wird zur Übertagung der Details zu einer Kostenposition verwendet.

    .. HINT::
        `Kostenposition JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/KostenpositionSchema.json>`_

    """

    # required attributes
    #: Ein Titel für die Zeile. Hier kann z.B. der Netzbetreiber eingetragen werden, wenn es sich um Netzkosten handelt.
    positionstitel: str = attrs.field(validator=attrs.validators.instance_of(str))

    betrag_kostenposition: Betrag = attrs.field(validator=attrs.validators.instance_of(Betrag))
    """Der errechnete Gesamtbetrag der Position als Ergebnis der Berechnung <Menge * Einzelpreis> oder
    <Einzelpreis / (Anzahl Tage Jahr) * zeitmenge>"""
    # todo: validate above calculation, see https://github.com/Hochfrequenz/BO4E-python/issues/282

    #: Bezeichnung für den Artikel für den die Kosten ermittelt wurden. Beispiel: Arbeitspreis HT
    artikelbezeichnung: str = attrs.field(validator=attrs.validators.instance_of(str))

    #: Der Preis für eine Einheit. Beispiele: 5,8200 ct/kWh oder 55 €/Jahr.
    einzelpreis: Preis = attrs.field(validator=attrs.validators.instance_of(Preis))

    # optional attributes
    #: inklusiver von-Zeitpunkt der Kostenzeitscheibe
    von: Optional[datetime] = attrs.field(
        default=None,
        validator=attrs.validators.optional([attrs.validators.instance_of(datetime), check_bis_is_later_than_von]),
    )
    #: exklusiver bis-Zeitpunkt der Kostenzeitscheibe
    bis: Optional[datetime] = attrs.field(
        default=None,
        validator=attrs.validators.optional([attrs.validators.instance_of(datetime), check_bis_is_later_than_von]),
    )

    #: Die Menge, die in die Kostenberechnung eingeflossen ist. Beispiel: 3.660 kWh
    menge: Optional[Menge] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Menge))
    )

    zeitmenge: Optional[Menge] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Menge))
    )
    """
    Wenn es einen zeitbasierten Preis gibt (z.B. €/Jahr), dann ist hier die Menge angegeben mit der die Kosten berechnet
    wurden. Z.B. 138 Tage.
    """

    #: Detaillierung des Artikels (optional). Beispiel: 'Drehstromzähler'
    artikeldetail: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
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
    betrag_kostenposition = fields.Nested(BetragSchema, data_key="betragKostenposition")
    artikelbezeichnung = fields.Str()
    einzelpreis = fields.Nested(PreisSchema)

    # optional attributes
    von = fields.DateTime(allow_none=True)
    bis = fields.DateTime(allow_none=True)
    menge = fields.Nested(MengeSchema, allow_none=True)
    zeitmenge = fields.Nested(MengeSchema, allow_none=True)
    artikeldetail = fields.Str(allow_none=True)
