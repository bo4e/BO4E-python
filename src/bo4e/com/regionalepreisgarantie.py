"""
Contains RegionalePreisgarantie class
and corresponding marshmallow schema for de-/serialization
"""


from marshmallow import fields

from bo4e.com.preisgarantie import Preisgarantie
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit


# pylint: disable=too-few-public-methods


class RegionalePreisgarantie(Preisgarantie):
    """
    Abbildung einer Preisgarantie mit regionaler Abgrenzung

    .. HINT::
        `RegionalePreisgarantie JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RegionalePreisgarantieSchema.json>`_

    """

    # required attributes
    #: Regionale Eingrenzung der Preisgarantie.
    regionale_gueltigkeit: RegionaleGueltigkeit
