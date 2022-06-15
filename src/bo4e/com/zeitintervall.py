"""
Contains Zeitintervall class
and corresponding marshmallow schema for de-/serialization
"""
import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.zeiteinheit import Zeiteinheit


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Zeitintervall(COM):
    """
    Abbildung für ein Zeitintervall. Die Abbildung eines Zeitintervalls.
    Z.B. zur Anwendung als Raster in äquidistanten Zeitreihen/Lastgängen, beispielsweise 15 Minuten.

    .. HINT::
        `Zeitintervall JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/ZeitintervallSchema.json>`_

    """

    # required attributes
    wert: int = attrs.field(validator=attrs.validators.instance_of(int))
    """
    Die Anzahl der Zeiteinheiten innerhalb  des Intervalls
    """
    zeiteinheit: Zeiteinheit = attrs.field(validator=attrs.validators.instance_of(Zeiteinheit))
    """
    Die Einheit des Zeitintervalls
    """


class ZeitintervallSchema(COMSchema):
    """
    Schema for de-/serialization of Zeitintervall.
    """

    class_name = Zeitintervall
    # required attributes
    wert = fields.Integer()
    zeiteinheit = EnumField(Zeiteinheit)
