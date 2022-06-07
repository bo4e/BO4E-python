"""
Contains Energiemix class
and corresponding marshmallow schema for de-/serialization
"""

from decimal import Decimal
from typing import List

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.energieherkunft import Energieherkunft, EnergieherkunftSchema
from bo4e.enum.oekolabel import Oekolabel
from bo4e.enum.oekozertifikat import Oekozertifikat
from bo4e.enum.sparte import Sparte
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attrs.define(auto_attribs=True, kw_only=True)
class Energiemix(COM):
    """
    Zusammensetzung der gelieferten Energie aus den verschiedenen Primärenergieformen.

    .. HINT::
        `Energiemix JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/EnergiemixSchema.json>`_

    """

    # required attributes
    #: Eindeutige Nummer zur Identifizierung des Energiemixes
    energiemixnummer: int = attrs.field(validator=attrs.validators.instance_of(int))
    #: Strom oder Gas etc.
    energieart: Sparte = attrs.field(validator=attrs.validators.instance_of(Sparte))
    #: Bezeichnung des Energiemix
    bezeichnung: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: Jahr, für das der Energiemix gilt
    gueltigkeitsjahr: int = attrs.field(validator=attrs.validators.instance_of(int))
    #: Anteile der jeweiligen Erzeugungsart
    anteil: List[Energieherkunft] = attrs.field(
        validator=[attrs.validators.instance_of(List), check_list_length_at_least_one]
    )

    # optional attributes
    #: Bemerkung zum Energiemix
    bemerkung: str = attrs.field(default=None)
    #: Höhe des erzeugten CO2-Ausstosses in g/kWh
    co2_emission: Decimal = attrs.field(default=None)
    #: Höhe des erzeugten Atommülls in g/kWh
    atommuell: Decimal = attrs.field(default=None)
    #: Zertifikate für den Energiemix
    oekozertifikate: List[Oekozertifikat] = attrs.field(default=[])
    #: Ökolabel für den Energiemix
    oekolabel: List[Oekolabel] = attrs.field(default=[])
    #: Kennzeichen, ob der Versorger zu den Öko Top Ten gehört
    oeko_top_ten: bool = attrs.field(default=None)
    #: Internetseite, auf der die Strommixdaten veröffentlicht sind
    website: str = attrs.field(default=None)


class EnergiemixSchema(COMSchema):
    """
    Schema for de-/serialization of Energiemix.
    """

    class_name = Energiemix
    # required attributes
    energiemixnummer = fields.Int()
    energieart = EnumField(Sparte)
    bezeichnung = fields.Str()
    gueltigkeitsjahr = fields.Int()
    anteil = fields.List(fields.Nested(EnergieherkunftSchema))

    # optional attributes
    bemerkung = fields.Str(load_default=None)
    co2_emission = fields.Decimal(load_default=None, as_string=True, data_key="co2Emission")
    atommuell = fields.Decimal(load_default=None, as_string=True)
    oekozertifikate = fields.List(EnumField(Oekozertifikat), load_default=None)
    oekolabel = fields.List(EnumField(Oekolabel), load_default=None)
    oeko_top_ten = fields.Bool(load_default=None, data_key="oekoTopTen")
    website = fields.Str(load_default=None)
