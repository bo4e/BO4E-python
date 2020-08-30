from dataclasses import dataclass, field

from dataclasses_json import LetterCase, dataclass_json

from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt, _GeschaeftsobjektDefaultBase, _GeschaeftsobjektBase


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


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(eq=True)
class Marktlokation(Geschaeftsobjekt, _MarktlokationDefaultBase, _MarktlokationBase):
    """
    Objekt zur Aufnahme der Informationen zu einer Marktlokation
    """
    pass
