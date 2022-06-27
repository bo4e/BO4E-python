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

    .. graphviz:: /api/dots/bo4e/com/RegionalePreisgarantie.dot

    """

    # required attributes
    #: Regionale Eingrenzung der Preisgarantie.
    regionale_gueltigkeit: RegionaleGueltigkeit
