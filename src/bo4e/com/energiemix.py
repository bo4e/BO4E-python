"""
Contains Energiemix class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import List

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.energieherkunft import Energieherkunft, EnergieherkunftSchema
from bo4e.enum.oekolabel import Oekolabel
from bo4e.enum.oekozertifikat import Oekozertifikat
from bo4e.enum.sparte import Sparte
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attr.s(auto_attribs=True, kw_only=True)
class Energiemix(COM):
    """
    Zusammensetzung der gelieferten Energie aus den verschiedenen Primärenergieformen.
    """

    # required attributes
    #: Eindeutige Nummer zur Identifizierung des Energiemixes
    energiemixnummer: int = attr.ib(validator=attr.validators.instance_of(int))
    #: Strom oder Gas etc.
    energieart: Sparte = attr.ib(validator=attr.validators.instance_of(Sparte))
    #: Bezeichnung des Energiemix
    bezeichnung: str = attr.ib(validator=attr.validators.instance_of(str))
    #: Jahr, für das der Energiemix gilt
    gueltigkeitsjahr: int = attr.ib(validator=attr.validators.instance_of(int))
    #: Anteile der jeweiligen Erzeugungsart
    anteil: List[Energieherkunft] = attr.ib(
        validator=[attr.validators.instance_of(List), check_list_length_at_least_one]
    )

    # optional attributes
    #: Bemerkung zum Energiemix
    bemerkung: str = attr.ib(default=None)
    #: Höhe des erzeugten CO2-Ausstosses in g/kWh
    co2_emission: Decimal = attr.ib(default=None)
    #: Höhe des erzeugten Atommülls in g/kWh
    atommuell: Decimal = attr.ib(default=None)
    #: Zertifikate für den Energiemix
    oekozertifikate: List[Oekozertifikat] = attr.ib(default=[])
    #: Ökolabel für den Energiemix
    oekolabel: List[Oekolabel] = attr.ib(default=[])
    #: Kennzeichen, ob der Versorger zu den Öko Top Ten gehört
    oeko_top_ten: bool = attr.ib(default=None)
    #: Internetseite, auf der die Strommixdaten veröffentlicht sind
    website: str = attr.ib(default=None)


class EnergiemixSchema(COMSchema):
    """
    Schema for de-/serialization of Energiemix.
    """

    # required attributes
    energiemixnummer = fields.Int()
    energieart = EnumField(Sparte)
    bezeichnung = fields.Str()
    gueltigkeitsjahr = fields.Int()
    anteil = fields.List(fields.Nested(EnergieherkunftSchema))

    # optional attributes
    bemerkung = fields.Str(load_default=None)
    co2_emission = fields.Decimal(load_default=None, as_string=True)
    atommuell = fields.Decimal(load_default=None, as_string=True)
    oekozertifikate = fields.List(EnumField(Oekozertifikat), load_default=None)
    oekolabel = fields.List(EnumField(Oekolabel), load_default=None)
    oeko_top_ten = fields.Bool(load_default=None)
    website = fields.Str(load_default=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Energiemix:
        """Deserialize JSON to Energiemix object"""
        return Energiemix(**data)
