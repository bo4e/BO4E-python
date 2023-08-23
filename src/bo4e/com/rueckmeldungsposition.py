"""Contains class Rueckmeldeposition"""
from typing import Optional

from pydantic import model_validator

from bo4e.com.abweichungsposition import Abweichungsposition
from bo4e.com.com import COM


class Rueckmeldungsposition(COM):
    """Zur Angabe einer Rückmeldung einer einzelnen Position."""

    # optional attributes
    positionsnummer: Optional[str] = None  #: Positionsnummer der Referenzierung
    abweichungspositionen: Optional[list[Abweichungsposition]] = None  #: Abweichungspositionen

    #: model validator for !XOR pos.nr. and abweichungspos.
    @model_validator(mode="after")
    def _field_combination_xor(self) -> "Rueckmeldungsposition":
        if (self.positionsnummer and self.abweichungspositionen is None) or (
            self.abweichungspositionen and self.positionsnummer is None
        ):
            raise ValueError("Attributes missing")
        return self
