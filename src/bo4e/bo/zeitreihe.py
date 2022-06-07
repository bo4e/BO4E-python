"""
Contains Zeitreihe class and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, GeschaeftsobjektSchema
from bo4e.com.zeitreihenwert import Zeitreihenwert, ZeitreihenwertSchema
from bo4e.enum.botyp import BoTyp
from bo4e.enum.medium import Medium
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.messart import Messart
from bo4e.enum.messgroesse import Messgroesse
from bo4e.enum.wertermittlungsverfahren import Wertermittlungsverfahren
from bo4e.validators import check_list_length_at_least_one


# pylint: disable=too-few-public-methods, too-many-instance-attributes
@attrs.define(auto_attribs=True, kw_only=True)
class Zeitreihe(Geschaeftsobjekt):
    """
    Abbildung einer allgemeinen Zeitreihe mit einem Wertvektor.
    Die Werte können mit wahlfreier zeitlicher Distanz im Vektor abgelegt sein.

    .. HINT::
        `Zeitreihe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/ZeitreiheSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = attrs.field(default=BoTyp.ZEITREIHE)
    #: Bezeichnung für die Zeitreihe
    bezeichnung: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: Beschreibt, was gemessen wurde (z.B. Strom, Spannung, Wirkleistung, Scheinleistung)
    messgroesse: Messgroesse = attrs.field(validator=attrs.validators.instance_of(Messgroesse))
    #: Beschreibt die Art der Messung (z.B. aktueller Wert, mittlerer Wert, maximaler Wert)
    messart: Messart = attrs.field(validator=attrs.validators.instance_of(Messart))
    #: Medium, das gemessen wurde (z.B. Wasser, Dampf, Strom, Gas)
    medium: Medium = attrs.field(validator=attrs.validators.instance_of(Medium))
    #: Alle Werte in der Tabelle haben die Einheit, die hier angegeben ist
    einheit: Mengeneinheit = attrs.field(validator=attrs.validators.instance_of(Mengeneinheit))

    #: Hier liegen jeweils die Werte
    werte: List[Zeitreihenwert] = attrs.field(
        validator=attrs.validators.deep_iterable(
            member_validator=attrs.validators.instance_of(Zeitreihenwert),
            iterable_validator=check_list_length_at_least_one,
        )
    )
    # optional attributes
    #: Beschreibt die Verwendung der Zeitreihe
    beschreibung: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )
    #: Version der Zeitreihe
    version: Optional[str] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(str))
    )
    #: Kennzeichnung, wie die Werte entstanden sind, z.B. durch Messung
    wertherkunft: Optional[Wertermittlungsverfahren] = attrs.field(
        default=None, validator=attrs.validators.optional(attrs.validators.instance_of(Wertermittlungsverfahren))
    )


class ZeitreiheSchema(GeschaeftsobjektSchema):
    """
    Schema for de-/serialization of Zeitreihe
    """

    class_name = Zeitreihe
    bezeichnung = fields.Str()
    messgroesse = EnumField(Messgroesse)
    messart = EnumField(Messart)
    medium = EnumField(Medium)
    einheit = EnumField(Mengeneinheit)
    werte = fields.List(fields.Nested(ZeitreihenwertSchema))

    # optional attributes
    beschreibung = fields.Str(load_default=None)
    version = fields.Str(load_default=None)
    wertherkunft = EnumField(Wertermittlungsverfahren, load_default=None)
