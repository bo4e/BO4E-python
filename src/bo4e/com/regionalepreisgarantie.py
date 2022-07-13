"""
Contains RegionalePreisgarantie class
and corresponding marshmallow schema for de-/serialization
"""


from bo4e.com.preisgarantie import Preisgarantie
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit

# pylint: disable=too-few-public-methods


class RegionalePreisgarantie(Preisgarantie):
    """
    Abbildung einer Preisgarantie mit regionaler Abgrenzung

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionalePreisgarantie.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionalePreisgarantie JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RegionalePreisgarantie.json>`_

    """

    # required attributes
    #: Regionale Eingrenzung der Preisgarantie.
    regionale_gueltigkeit: RegionaleGueltigkeit
