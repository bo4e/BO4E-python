"""
Contains base class for all business objects
and corresponding marshmallow schema for de-/serialization
"""
# pylint: disable=unused-argument, too-few-public-methods
from typing import List, Optional, Type

import attr
from marshmallow import Schema, fields, post_load
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.externereferenz import ExterneReferenz, ExterneReferenzSchema
from bo4e.enum.botyp import BoTyp


def _create_empty_referenzen_list() -> List[ExterneReferenz]:
    """
    A method with a type hint to please mypy
    https://stackoverflow.com/a/61281305/10009545
    :return:
    """
    return []


@attr.s(auto_attribs=True, kw_only=True)
class Geschaeftsobjekt:  # Base class for all business objects
    """
    Das BO Geschäftsobjekt ist der Master für alle Geschäftsobjekte.
    Alle Attribute, die hier in diesem BO enthalten sind, werden an alle BOs vererbt.
    """

    # required attributes
    versionstruktur: str = attr.ib(default="2")  #: Version der BO-Struktur aka "fachliche Versionierung"
    bo_typ: BoTyp = attr.ib(default=BoTyp.GESCHAEFTSOBJEKT)  #: Der Typ des Geschäftsobjektes
    # bo_typ is used as discriminator f.e. for databases or deserialization

    # optional attributes
    externe_referenzen: Optional[List[ExterneReferenz]] = attr.ib(
        default=_create_empty_referenzen_list(), validator=attr.validators.instance_of(List)  # type:ignore[arg-type]
    )  #: Hier können IDs anderer Systeme hinterlegt werden (z.B. eine SAP-GP-Nummer oder eine GUID)


class GeschaeftsobjektSchema(Schema):
    """
    This is an "abstract" class.
    All business objects schemata do inherit from this class.
    """

    # class_name is needed to use the correct schema for deserialization.
    class_name: Type[Geschaeftsobjekt] = Geschaeftsobjekt

    # required attributes
    versionstruktur = fields.String()
    bo_typ = EnumField(BoTyp, data_key="boTyp")

    # optional attributes
    externe_referenzen = fields.List(
        fields.Nested(ExterneReferenzSchema), data_key="externeReferenzen", load_default=None
    )

    @post_load
    def deserialize(self, data, **kwargs):
        """Deserialize JSON to python object."""
        return type(self).class_name(**data)
