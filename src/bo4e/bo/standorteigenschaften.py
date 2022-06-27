"""
Contains Standorteigenschaften class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import conlist

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.standorteigenschaftenallgemein import StandorteigenschaftenAllgemein
from bo4e.com.standorteigenschaftengas import StandorteigenschaftenGas
from bo4e.com.standorteigenschaftenstrom import StandorteigenschaftenStrom
from bo4e.enum.botyp import BoTyp


class Standorteigenschaften(Geschaeftsobjekt):
    """
    Modelliert die regionalen und spartenspezifischen Eigenschaften einer gegebenen Adresse.

    .. graphviz:: /api/dots/bo4e/bo/Standorteigenschaften.dot

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.STANDORTEIGENSCHAFTEN
    #: Allgemeine Eigenschaften
    eigenschaften_allgemein: StandorteigenschaftenAllgemein
    #: Eigenschaften zur Sparte Strom
    eigenschaften_strom: conlist(StandorteigenschaftenStrom, min_items=1)

    # optional attributes
    #: Eigenschaften zur Sparte Gas
    eigenschaften_gas: StandorteigenschaftenGas = None
