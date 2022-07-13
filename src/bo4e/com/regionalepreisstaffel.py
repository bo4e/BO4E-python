"""
Contains RegionalePreisstaffel class and corresponding marshmallow schema for de-/serialization
"""


from bo4e.com.preisstaffel import Preisstaffel
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit

# pylint: disable=too-few-public-methods


class RegionalePreisstaffel(Preisstaffel):
    """
    Abbildung einer Preisstaffel mit regionaler Abgrenzung

    .. raw:: html

        <object data="../_static/images/bo4e/com/RegionalePreisstaffel.svg" type="image/svg+xml"></object>

    .. HINT::
        `RegionalePreisstaffel JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/RegionalePreisstaffel.json>`_

    """

    # required attributes
    #: Regionale Eingrenzung der Preisstaffel
    regionale_gueltigkeit: RegionaleGueltigkeit
