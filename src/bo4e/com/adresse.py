"""
Contains Adresse class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM
from bo4e.enum.landescode import Landescode
from pydantic import validator, StrictStr


# pylint: disable=too-many-instance-attributes, too-few-public-methods


class Adresse(COM):
    """
    Contains an address that can be used for most purposes.

    .. HINT::
        `Adresse JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AdresseSchema.json>`_

    """

    # required attributes
    #: Die Postleitzahl; z.B: "41836"
    postleitzahl: str
    #: Bezeichnung der Stadt; z.B. "Hückelhoven"
    ort: str

    # optional attributes
    #: Bezeichnung der Straße; z.B. "Weserstraße"
    strasse: str = None
    #: Hausnummer inkl. Zusatz; z.B. "3", "4a"
    hausnummer: str = None
    #: Im Falle einer Postfachadresse das Postfach; Damit werden Straße und Hausnummer nicht berücksichtigt
    postfach: str = None
    #: Zusatzhinweis zum Auffinden der Adresse, z.B. "3. Stock linke Wohnung"
    adresszusatz: str = None
    #: Im Falle einer c/o-Adresse steht in diesem Attribut die Anrede. Z.B. "c/o Veronica Hauptmieterin"
    co_ergaenzung: str = None
    #: Offizieller ISO-Landescode
    landescode: Landescode = Landescode.DE  # type:ignore

    @validator("postfach", always=True)
    def strasse_xor_postfach(cls, v, values):
        """
        An address is valid if it contains a postfach XOR (a strasse AND hausnummer).
        This functions checks for these conditions of a valid address.

        Nur folgende Angabekombinationen sind (nach der Abfrage) möglich:
        Straße           w
        Hausnummer       w
        Postfach         w
        Postleitzahl
        Ort
        """
        if values["strasse"] and values["hausnummer"] and not v or not values["strasse"] and not values["hausnummer"]:
            return v
        else:
            raise ValueError('You have to define either "strasse" and "hausnummer" or "postfach".')
