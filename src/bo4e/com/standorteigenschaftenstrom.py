"""
Contains StandorteigenschaftenStrom class
and corresponding marshmallow schema for de-/serialization
"""

import attrs
from marshmallow import fields

from bo4e.com.com import COM


# pylint: disable=too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class StandorteigenschaftenStrom(COM):
    """
    Standorteigenschaften der Sparte Strom

    .. HINT::
        `StandorteigenschaftenStrom JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/StandorteigenschaftenStromSchema.json>`_

    """

    # required attributes
    #: Die EIC-Nummer des Bilanzierungsgebietes
    bilanzierungsgebiet_eic: str
    # todo: use EIC validation: https://github.com/Hochfrequenz/BO4E-python/issues/147

    #: Der Name der Regelzone
    regelzone: str

    #: De EIC-Nummer der Regelzone
    regelzone_eic: str
    # todo: use EIC validation: https://github.com/Hochfrequenz/BO4E-python/issues/147


class StandorteigenschaftenStromSchema(COMSchema):
    """
    Schema for de-/serialization of StandorteigenschaftenStrom.
    """

    class_name = StandorteigenschaftenStrom
    # required attributes
    bilanzierungsgebiet_eic = fields.Str(data_key="bilanzierungsgebietEic")
    regelzone = fields.Str()
    regelzone_eic = fields.Str(data_key="regelzoneEic")
