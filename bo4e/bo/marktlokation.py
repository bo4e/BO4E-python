from abc import ABC
from dataclasses import dataclass

from dataclasses_json import LetterCase, dataclass_json

from bo4e.bo.geschaeftsobjekt import (
    Geschaeftsobjekt,
    _GeschaeftsobjektDefaultBase,
    _GeschaeftsobjektBase,
)
from bo4e.com.adresse import Adresse
from bo4e.enum.sparte import Sparte


@dataclass
class _MarktlokationDefaultBase(_GeschaeftsobjektDefaultBase):
    """
    holds default values for Marktlokations
    """

    bo_typ: str = "MARKTLOKATION"


@dataclass
class _MarktlokationBase(_GeschaeftsobjektBase):
    """
    holds those values that do not have a default value
    """

    marktlokations_id: str
    sparte: Sparte
    lokationsadresse: Adresse


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(eq=True)
class Marktlokation(
    ABC, Geschaeftsobjekt, _MarktlokationDefaultBase, _MarktlokationBase
):
    """
    Objekt zur Aufnahme der Informationen zu einer Marktlokation
    """

    pass
