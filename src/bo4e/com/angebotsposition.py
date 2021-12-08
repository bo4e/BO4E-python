"""
Contains Angebotsposition class
and corresponding marshmallow schema for de-/serialization
"""

import attr
from marshmallow import fields, post_load

from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.menge import Menge, MengeSchema
from bo4e.com.preis import Preis, PreisSchema


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Angebotsposition(COM):
    """
    Unterhalb von Angebotsteilen sind die Angebotspositionen eingebunden.
    Hier werden die angebotenen Bestandteile einzeln aufgeführt. Beispiel:
    Positionsmenge: 4000 kWh
    Positionspreis: 24,56 ct/kWh
    Positionskosten: 982,40 EUR
    """

    # required attributes
    #: Bezeichnung der jeweiligen Position des Angebotsteils
    positionsbezeichnung: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Preis pro Einheit/Stückpreis des angebotenen Artikels.
    positionspreis: Preis = attr.ib(validator=attr.validators.instance_of(Preis))

    # optional attributes
    #: Menge des angebotenen Artikels (z.B. Wirkarbeit in kWh), in dieser Angebotsposition
    positionsmenge: Menge = attr.ib(default=None, validator=attr.validators.instance_of(Menge))
    #: Kosten (positionspreis * positionsmenge) für diese Angebotsposition
    positionskosten: Betrag = attr.ib(default=None, validator=attr.validators.instance_of(Betrag))

    # for a preis = menge*times validation we first need to resolve
    # https://github.com/Hochfrequenz/BO4E-python/issues/126


class AngebotspositionSchema(COMSchema):
    """
    Schema for de-/serialization of Angebotsposition.
    """

    # required attributes
    positionsbezeichnung = fields.String()
    positionspreis = fields.Nested(PreisSchema)
    positionsmenge = fields.Nested(MengeSchema, load_default=None)
    positionskosten = fields.Nested(BetragSchema, load_default=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Angebotsposition:
        """Deserialize JSON to Angebotsposition object"""
        return Angebotsposition(**data)
