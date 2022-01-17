"""
Contains Lastgang and LastgangKompakt class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.com.tagesvektor import Tagesvektor, TagesvektorSchema
from bo4e.com.zeitintervall import Zeitintervall, ZeitintervallSchema
from bo4e.com.zeitreihenwert import Zeitreihenwert, ZeitreihenwertSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.lokationstyp import Lokationstyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.sparte import Sparte
from bo4e.validators import check_list_length_at_least_one, obis_validator


# pylint: disable=too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class _LastgangBody:
    """
    The LastgangBody is a mixin that contains the "body" of a Lastgang that is used in both the :class:`Lastgang` as
    well as :class:`LastgangKompakt`.
    """

    #: Angabe, ob es sich um einen Gas- oder Stromlastgang handelt
    sparte: Sparte = attr.ib(validator=attr.validators.instance_of(Sparte))

    #: Eindeutige Nummer der Marktlokation bzw der Messlokation, zu der der Lastgang gehört
    lokations_id: str = attr.ib(validator=attr.validators.instance_of(str))

    #: Marktlokation oder Messlokation
    lokationstyp: str = attr.ib(validator=attr.validators.instance_of(Lokationstyp))
    # todo: implement a lokations-id + lokationstyp cross check (such that lokationstyp malo checks for valid malo id)
    # https://github.com/Hochfrequenz/BO4E-python/issues/321

    #: Definition der gemessenen Größe anhand ihrer Einheit
    messgroesse: Mengeneinheit = attr.ib(validator=attr.validators.instance_of(Mengeneinheit))

    # optional attributes
    #: Versionsnummer des Lastgangs
    version: Optional[str] = attr.ib(default=None, validator=attr.validators.optional(attr.validators.instance_of(str)))
    #: Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:1.8.1'
    obis_kennzahl: Optional[str] = attr.ib(default=None, validator=attr.validators.optional(obis_validator))


# pylint: disable=too-many-instance-attributes, too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class LastgangKompakt(Geschaeftsobjekt, _LastgangBody):
    """
    Modell zur Abbildung eines kompakten Lastganges.
    In diesem Modell werden die Messwerte in Form von Tagesvektoren mit fester Anzahl von Werten übertragen.
    Daher ist dieses BO nur zur Übertragung von äquidistanten Messwertverläufen geeignet.
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.LASTGANG_KOMPAKT)

    #: Angabe des Rasters innerhalb aller Tagesvektoren dieses Lastgangs
    zeitintervall: Zeitintervall = attr.ib(validator=attr.validators.instance_of(Zeitintervall))
    # todo: implement a cross check that this zeitintervall is actually the one used in tagesvektoren
    # https://github.com/Hochfrequenz/BO4E-python/issues/322

    #: Die im Lastgang enthaltenen Messwerte in Form von Tagesvektoren
    tagesvektoren: List[Tagesvektor] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Tagesvektor),
            iterable_validator=attr.validators.instance_of(list),
        )
    )


# pylint: disable=too-many-instance-attributes, too-few-public-methods
@attr.s(auto_attribs=True, kw_only=True)
class Lastgang(Geschaeftsobjekt, _LastgangBody):
    """
    Modell zur Abbildung eines Lastganges;
    In diesem Modell werden die Messwerte mit einem vollständigen Zeitintervall angegeben und es bietet daher eine hohe
    Flexibilität in der Übertragung jeglicher zeitlich veränderlicher Messgrössen.
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.LASTGANG)

    #: Die im Lastgang enthaltenen Messwerte
    werte: List[Zeitreihenwert] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Zeitreihenwert),
            iterable_validator=check_list_length_at_least_one,
        )
    )


class _LastgangBodySchemaMixin:
    """
    A mixin for schemas to deserialize Lastgang and LastgangKompakt objects.
    """

    sparte = EnumField(Sparte)
    lokations_id = fields.Str()
    lokationstyp = EnumField(Lokationstyp)
    messgroesse = EnumField(Mengeneinheit)

    # optional attributes
    obis_kennzahl = fields.Str(load_default=None)
    version = fields.Str(allow_none=True)


class LastgangKompaktSchema(GeschaeftsobjektSchema, _LastgangBodySchemaMixin):
    """
    Schema for de-/serialization of LastgangKompakt
    """

    class_name = LastgangKompakt
    # required attributes
    zeitintervall = fields.Nested(ZeitintervallSchema)
    tagesvektoren = fields.List(fields.Nested(TagesvektorSchema))


class LastgangSchema(GeschaeftsobjektSchema, _LastgangBodySchemaMixin):
    """
    Schema for de-/serialization of Lastgang
    """

    class_name = Lastgang
    # required attributes
    werte = fields.List(fields.Nested(ZeitreihenwertSchema))
