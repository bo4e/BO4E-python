"""
Contains LastgangKompakt class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional, Type

import attr
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.com.adresse import Adresse, AdresseSchema
from bo4e.com.tagesvektor import Tagesvektor
from bo4e.com.zeitintervall import Zeitintervall
from bo4e.enum.anrede import Anrede
from bo4e.enum.botyp import BoTyp
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.kontaktart import Kontaktart

# pylint: disable=too-many-instance-attributes, too-few-public-methods
from bo4e.enum.lokationstyp import Lokationstyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.sparte import Sparte
from bo4e.validators import obis_validator


@attr.s(auto_attribs=True, kw_only=True)
class LastgangKompakt(Geschaeftsobjekt):
    """ "
    Modell zur Abbildung eines kompakten Lastganges.
    In diesem Modell werden die Messwerte in Form von Tagesvektoren mit fester Anzahl von Werten übertragen.
    Daher ist dieses BO nur zur Übertragung von äquidistanten Messwertverläufen geeignet.
    """

    # required attributes
    bo_typ: BoTyp = attr.ib(default=BoTyp.LASTGANG_KOMPAKT)
    #: Angabe, ob es sich um einen Gas- oder Stromlastgang handelt
    sparte: Sparte = attr.ib(validator=attr.validators.instance_of(Sparte))

    #: Eindeutige Nummer der Marktlokation bzw der Messlokation, zu der der Lastgang gehört
    lokations_id: str = attr.ib(validator=attr.validators.instance_of(str))

    #: Marktlokation oder Messlokation
    lokationstyp: str = attr.ib(validator=attr.validators.instance_of(Lokationstyp))
    # todo: implement a lokations-id + lokationstyp cross check (such that lokationstyp malo checks for valid malo id)

    #: Definition der gemessenen Größe anhand ihrer Einheit
    messgroesse: Mengeneinheit = attr.ib(validator=attr.validators.instance_of(Mengeneinheit))

    #: Angabe des Rasters innerhalb aller Tagesvektoren dieses Lastgangs
    zeitintervall: Zeitintervall = attr.ib(validator=attr.validators.instance_of(Zeitintervall))
    # todo: implement a cross check that this zeitintervall is actually the one used in tagesvektoren

    #: Die OBIS-Kennzahl für den Wert, die festlegt, welche Größe mit dem Stand gemeldet wird, z.B. '1-0:1.8.1'
    obis_kennzahl: str = attr.ib(validator=obis_validator)

    #: Die im Lastgang enthaltenen Messwerte in Form von Tagesvektoren
    tagesvektoren: List[Tagesvektor] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Tagesvektor),
            iterable_validator=attr.validators.instance_of(list),
        )
    )
