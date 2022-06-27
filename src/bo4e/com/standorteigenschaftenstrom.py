"""
Contains StandorteigenschaftenStrom class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM


# pylint: disable=too-few-public-methods


class StandorteigenschaftenStrom(COM):
    """
    Standorteigenschaften der Sparte Strom

    .. graphviz:: /api/dots/bo4e/com/StandorteigenschaftenStrom.dot

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
