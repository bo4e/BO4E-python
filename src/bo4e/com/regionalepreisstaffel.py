"""
Contains RegionalePreisstaffel class and corresponding marshmallow schema for de-/serialization
"""


from marshmallow import fields

from bo4e.com.preisstaffel import Preisstaffel
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit


# pylint: disable=too-few-public-methods


class RegionalePreisstaffel(Preisstaffel):
    """
    Abbildung einer Preisstaffel mit regionaler Abgrenzung

    .. HINT::
        `RegionalePreisstaffel JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RegionalePreisstaffelSchema.json>`_

    """

    # required attributes
    #: Regionale Eingrenzung der Preisstaffel
    regionale_gueltigkeit: RegionaleGueltigkeit
