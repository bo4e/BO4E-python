from abc import ABC
from dataclasses import dataclass

from dataclasses_json import LetterCase, dataclass_json


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class COM(ABC):
    """
    abstract base class for all components
    """
