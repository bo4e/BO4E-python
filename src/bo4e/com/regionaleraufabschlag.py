"""
Contains RegionalerAufAbschlag class and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional

import attr
from marshmallow import fields, post_load

from bo4e.bo.marktlokation import Marktlokation, MarktlokationSchema
from bo4e.com.angebotsposition import Angebotsposition, AngebotspositionSchema
from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.com.com import COM, COMSchema
from bo4e.com.menge import Menge, MengeSchema
from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class RegionalerAufAbschlag(COM):
    """
    Mit dieser Komponente können Auf- und Abschläge verschiedener Typen im Zusammenhang mit regionalen Gültigkeiten
    abgebildet werden.
    Hier sind auch die Auswirkungen auf verschiedene Tarifparameter modelliert, die sich durch die Auswahl eines Auf-
    oder Abschlags ergeben.
    """

    # required attributes
    #: Einzelne Positionen, die zu diesem Angebotsteil gehören
    bezeichnung: str = attr.ib(validator=attr.validators.instance_of(str))

    #: Werte für die gestaffelten Auf/Abschläge mit regionaler Eingrenzung
    staffeln: List[RegionalePreisstaffel] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(RegionalePreisstaffel),
            iterable_validator=check_list_length_at_least_one,
        )
    )


class AngebotsteilSchema(COMSchema):
    """
    Schema for de-/serialization of Angebotsteil.
    """

    # required attributes
    positionen = fields.List(fields.Nested(AngebotspositionSchema))

    # optional attributes
    anfrage_subreferenz = fields.Str(load_default=None)
    lieferstellenangebotsteil = fields.List(fields.Nested(MarktlokationSchema), load_default=None)
    gesamtmengeangebotsteil = fields.Nested(MengeSchema, load_default=None)
    gesamtkostenangebotsteil = fields.Nested(BetragSchema, load_default=None)
    lieferzeitraum = fields.Nested(ZeitraumSchema, load_default=None)

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> Angebotsteil:
        """Deserialize JSON to Angebotsteil object"""
        return Angebotsteil(**data)
