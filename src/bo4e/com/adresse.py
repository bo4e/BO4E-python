"""
Contains Adresse class
and corresponding marshmallow schema for de-/serialization
"""

import attrs
from marshmallow import fields
from marshmallow_enum import EnumField  # type:ignore[import]

from bo4e.com.com import COM, COMSchema
from bo4e.enum.landescode import Landescode


# pylint: disable=unused-argument
def strasse_xor_postfach(instance, attribute, value):
    """
    An address is valid if it contains a postfach XOR (a strasse AND hausnummer).
    This functions checks for these conditions of a valid address.
    """
    if instance.strasse or instance.hausnummer:
        if instance.postfach:
            raise ValueError("Enter either strasse and hausnummer OR postfach.")
        if not instance.strasse:
            raise ValueError("Missing strasse to hausnummer.")
        if not instance.hausnummer:
            raise ValueError("Missing hausnummer to strasse.")


# pylint: disable=too-many-instance-attributes, too-few-public-methods
@attrs.define(auto_attribs=True, kw_only=True)
class Adresse(COM):
    """
    Contains an address that can be used for most purposes.

    .. HINT::
        `Adresse JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AdresseSchema.json>`_

    """

    # required attributes
    #: Die Postleitzahl; z.B: "41836"
    postleitzahl: str = attrs.field(validator=attrs.validators.instance_of(str))
    #: Bezeichnung der Stadt; z.B. "Hückelhoven"
    ort: str = attrs.field(validator=attrs.validators.instance_of(str))

    # optional attributes
    #: Bezeichnung der Straße; z.B. "Weserstraße"
    strasse: str = attrs.field(default=None, validator=strasse_xor_postfach)
    #: Hausnummer inkl. Zusatz; z.B. "3", "4a"
    hausnummer: str = attrs.field(default=None, validator=strasse_xor_postfach)
    #: Im Falle einer Postfachadresse das Postfach; Damit werden Straße und Hausnummer nicht berücksichtigt
    postfach: str = attrs.field(default=None, validator=strasse_xor_postfach)
    #: Zusatzhinweis zum Auffinden der Adresse, z.B. "3. Stock linke Wohnung"
    adresszusatz: str = attrs.field(default=None)
    #: Im Falle einer c/o-Adresse steht in diesem Attribut die Anrede. Z.B. "c/o Veronica Hauptmieterin"
    co_ergaenzung: str = attrs.field(default=None)
    #: Offizieller ISO-Landescode
    landescode: Landescode = attrs.field(default=Landescode.DE)  # type:ignore


class AdresseSchema(COMSchema):
    """
    Schema for de-/serialization of Adresse.
    """

    class_name = Adresse

    # required attributes
    postleitzahl = fields.Str()
    ort = fields.Str()

    # optional attributes
    strasse = fields.Str(load_default=None)
    hausnummer = fields.Str(load_default=None)
    postfach = fields.Str(load_default=None)
    adresszusatz = fields.Str(load_default=None)
    co_ergaenzung = fields.Str(load_default=None, data_key="coErgaenzung")
    landescode = EnumField(Landescode)
