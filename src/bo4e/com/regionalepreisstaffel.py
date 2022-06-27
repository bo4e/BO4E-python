"""
Contains RegionalePreisstaffel class and corresponding marshmallow schema for de-/serialization
"""


from bo4e.com.preisstaffel import Preisstaffel
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit


# pylint: disable=too-few-public-methods


class RegionalePreisstaffel(Preisstaffel):
    """
    Abbildung einer Preisstaffel mit regionaler Abgrenzung

    .. graphviz:: /api/dots/bo4e/com/RegionalePreisstaffel.dot

    """

    # required attributes
    #: Regionale Eingrenzung der Preisstaffel
    regionale_gueltigkeit: RegionaleGueltigkeit
