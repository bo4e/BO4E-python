"""
Contains RegionaleGueltigkeit class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List

import attr
from marshmallow import fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.com.kriteriumwert import KriteriumWert, KriteriumWertSchema
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class RegionaleGueltigkeit(COM):
    """
    Mit dieser Komponente können regionale Gültigkeiten, z.B. für Tarife, Zu- und Abschläge und Preise definiert werden.
    """

    # required attributes
    gueltigkeitstyp: Gueltigkeitstyp = attr.ib(
        validator=attr.validators.in_(Gueltigkeitstyp)
    )  #: Unterscheidung ob Positivliste oder Negativliste übertragen wird
    kriteriums_werte: List[KriteriumWert] = attr.ib(
        validator=attr.validators.instance_of(list)
    )  #:  Hier stehen die Kriterien, die die regionale Gültigkeit festlegen

    @kriteriums_werte.validator
    # pylint: disable=unused-argument, no-self-use
    def check_list_length(self, attribute, value):
        """
        Check that minimal list length is at least one.
        """
        if len(value) < 1:
            raise ValueError("kriteriumswerte must not be empty.")


class RegionaleGueltigkeitSchema(COMSchema):
    """
    Schema for de-/serialization of RegionaleGueltigkeit.
    """

    # required attributes
    gueltigkeitstyp = EnumField(Gueltigkeitstyp)
    kriteriums_werte = fields.List(fields.Nested(KriteriumWertSchema))

    # pylint: disable=no-self-use, unused-argument
    @post_load
    def deserialize(self, data, **kwargs) -> RegionaleGueltigkeit:
        """Deserialize JSON to RegionaleGueltigkeit object"""
        return RegionaleGueltigkeit(**data)
