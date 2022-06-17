"""
Contains Standorteigenschaften class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional


from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.com.standorteigenschaftenallgemein import StandorteigenschaftenAllgemein
from bo4e.com.standorteigenschaftengas import StandorteigenschaftenGas
from bo4e.com.standorteigenschaftenstrom import StandorteigenschaftenStrom
from bo4e.enum.botyp import BoTyp


# pylint: disable=too-few-public-methods
from pydantic import conlist


class Standorteigenschaften(Geschaeftsobjekt):
    """
    Modelliert die regionalen und spartenspezifischen Eigenschaften einer gegebenen Adresse.

    .. HINT::
        `Standorteigenschaften JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/StandorteigenschaftenSchema.json>`_

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
