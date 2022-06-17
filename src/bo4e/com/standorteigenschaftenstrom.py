"""
Contains StandorteigenschaftenStrom class
and corresponding marshmallow schema for de-/serialization
"""
from pydantic import StrictStr

from bo4e.com.com import COM


# pylint: disable=too-few-public-methods


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
