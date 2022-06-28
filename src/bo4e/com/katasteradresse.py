"""
Contains Katasteradresse class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM


# pylint: disable=too-few-public-methods


class Katasteradresse(COM):
    """
    Dient der Adressierung über die Liegenschafts-Information.

    .. graphviz:: /api/dots/bo4e/com/Katasteradresse.dot

    .. HINT::
        `Katasteradresse JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Katasteradresse.json>`_

    """

    gemarkung_flur: str
    flurstueck: str
