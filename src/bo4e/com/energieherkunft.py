"""
Contains Energieherkunft class
and corresponding marshmallow schema for de-/serialization
"""
# pylint: disable=no-name-in-module
from pydantic import condecimal

from bo4e.com.com import COM
from bo4e.enum.erzeugungsart import Erzeugungsart

# pylint: disable=too-few-public-methods


class Energieherkunft(COM):
    """
    Abbildung einer Energieherkunft

    .. graphviz:: /api/dots/bo4e/com/Energieherkunft.dot

    """

    # required attributes
    #: Art der Erzeugung der Energie.
    erzeugungsart: Erzeugungsart
    #: Prozentualer Anteil der jeweiligen Erzeugungsart.
    anteil_prozent: condecimal(gt=0, lt=100)
