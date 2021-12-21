"""
Contains Fremdkostenposition and corresponding marshmallow schema for de-/serialization
"""
from datetime import datetime
from typing import Optional

import attr
from marshmallow import fields, post_load

from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.menge import Menge, MengeSchema
from bo4e.com.preis import Preis, PreisSchema


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attr.s(auto_attribs=True, kw_only=True)
class Fremdkostenposition(COM):
    """
    Eine Kostenposition im Bereich der Fremdkosten
    """

    # required attributes
    #: Ein Titel für die Zeile. Hier kann z.B. der Netzbetreiber eingetragen werden, wenn es sich um Netzkosten handelt
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
    von: Optional[datetime] = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(datetime)))
    #: exklusiver bis-Zeitpunkt der Kostenzeitscheibe
    bis: Optional[datetime] = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(datetime)))
    # todo: implement von/bis validation as soon as https://github.com/Hochfrequenz/BO4E-python/pull/266 is merged

    #: Die Menge, die in die Kostenberechnung eingeflossen ist. Beispiel: 3.660 kWh
    menge: Optional[Menge] = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(Menge)))

    zeitmenge: Optional[Menge] = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(Menge)))
    """
    Wenn es einen zeitbasierten Preis gibt (z.B. €/Jahr), dann ist hier die Menge angegeben mit der die Kosten berechnet
    wurden. Z.B. 138 Tage.
    """

    #: Detaillierung des Artikels (optional). Beispiel: 'Drehstromzähler'
    artikeldetail: Optional[str] = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))

    #: Der Name des Marktpartners, der die Preise festlegt, bzw. die Kosten in Rechnung stellt
    marktpartnername: Optional[str] = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))

    #: Die Codenummer (z.B. BDEW-Codenummer) des Marktpartners, der die Preise festlegt / die Kosten in Rechnung stellt
    marktpartnercode: Optional[str] = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))

    #: EIC-Code des Regel- oder Marktgebietes eingetragen. Z.B. '10YDE-EON------1' für die Regelzone TenneT
    gebietcode_eic: Optional[str] = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))
    # todo: see issue https://github.com/Hochfrequenz/BO4E-python/issues/147 for EIC validation

    #: Link zum veröffentlichten Preisblatt
    link_preisblatt: Optional[str] = attr.ib(validator=attr.validators.optional(attr.validators.instance_of(str)))


class FremdkostenpositionSchema(COMSchema):
    """
    Schema for de-/serialization of Fremdkostenposition
    """

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
    marktpartnername = fields.Str(allow_none=True)
    marktpartnercode = fields.Str(allow_none=True)
    gebietcode_eic = fields.Str(allow_none=True)
    link_preisblatt = fields.Str(allow_none=True)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Fremdkostenposition:
        """Deserialize JSON to Fremdkostenposition object"""
        return Fremdkostenposition(**data)
