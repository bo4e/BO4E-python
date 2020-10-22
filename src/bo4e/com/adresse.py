from dataclasses import dataclass, field

from dataclasses_json import dataclass_json, config

from bo4e.com.com import COM
from bo4e.enum.landescode import Landescode


@dataclass
class _AdresseDefaultBase:
    """
    holds default values for Adresse
    """

    postfach: str = None
    adresszusatz: str = None
    co_ergaenzung: str = None
    landescode: Landescode = field(
        default="DE", metadata=config(encoder=Landescode.json_encoder)
    )


@dataclass
class _AdresseBase:
    """
    holds those values that do not have a default value/are obligatory
    """

    postleitzahl: str
    ort: str
    strasse: str
    hausnummer: str


@dataclass_json
@dataclass
class Adresse(COM, _AdresseDefaultBase, _AdresseBase):
    """
    Enthält eine Adresse, die für die meisten Zwecke verwendbar ist.
    """
