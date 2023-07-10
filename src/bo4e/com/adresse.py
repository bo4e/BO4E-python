"""
Contains Adresse class
and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from pydantic import model_validator

from bo4e.com.com import COM
from bo4e.enum.landescode import Landescode

# pylint: disable=too-many-instance-attributes, too-few-public-methods


class Adresse(COM):
    """
    Contains an address that can be used for most purposes.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Adresse.svg" type="image/svg+xml"></object>

    .. HINT::
        `Adresse JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/Adresse.json>`_

    """

    # required attributes
    #: Die Postleitzahl; z.B: "41836"
    postleitzahl: str
    #: Bezeichnung der Stadt; z.B. "Hückelhoven"
    ort: str

    # optional attributes
    #: Bezeichnung des Ortsteils; z.B. "Mitte"
    ortsteil: Optional[str] = None
    #: Bezeichnung der Straße; z.B. "Weserstraße"
    strasse: Optional[str] = None
    #: Hausnummer inkl. Zusatz; z.B. "3", "4a"
    hausnummer: Optional[str] = None
    #: Im Falle einer Postfachadresse das Postfach; Damit werden Straße und Hausnummer nicht berücksichtigt
    postfach: Optional[str] = None
    #: Zusatzhinweis zum Auffinden der Adresse, z.B. "3. Stock linke Wohnung"
    adresszusatz: Optional[str] = None
    #: Im Falle einer c/o-Adresse steht in diesem Attribut die Anrede. Z.B. "c/o Veronica Hauptmieterin"
    co_ergaenzung: Optional[str] = None
    #: Offizieller ISO-Landescode
    landescode: Landescode = Landescode.DE  # type:ignore

    # pylint: disable=no-self-argument
    @model_validator(mode="after")  # type:ignore[arg-type]
    @classmethod
    def strasse_xor_postfach(cls, model: "Adresse") -> "Adresse":
        """
        An address is valid if it contains a postfach XOR (a strasse AND hausnummer).
        This functions checks for these conditions of a valid address.

        Nur folgende Angabekombinationen sind (nach der Abfrage) möglich:
        Straße           w   f   f
        Hausnummer       w   f   f
        Postfach         f   w   f
        Postleitzahl     w   w   w
        Ort              w   w   w
        """
        if model.strasse and model.hausnummer and not model.postfach or not model.strasse and not model.hausnummer:
            return model
        raise ValueError('You have to define either "strasse" and "hausnummer" or "postfach".')
