"""
Contains Adresse class
"""

from typing import Annotated, Literal, Optional

from pydantic import Field

from ..enum.comtyp import ComTyp
from ..enum.landescode import Landescode
from ..utils import postprocess_docstring
from .com import COM

# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class Adresse(COM):
    """
    Contains an address that can be used for most purposes.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Adresse.svg" type="image/svg+xml"></object>

    .. HINT::
        `Adresse JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Adresse.json>`_

    """

    typ: Annotated[Literal[ComTyp.ADRESSE], Field(alias="_typ")] = ComTyp.ADRESSE

    postleitzahl: Optional[str] = None
    """
    Die Postleitzahl; z.B: "41836"
    """
    ort: Optional[str] = None
    """
    Bezeichnung der Stadt; z.B. "Hückelhoven"
    """

    ortsteil: Optional[str] = None
    """
    Bezeichnung des Ortsteils; z.B. "Mitte"
    """
    strasse: Optional[str] = None
    """
    Bezeichnung der Straße; z.B. "Weserstraße"
    """
    hausnummer: Optional[str] = None
    """
    Hausnummer inkl. Zusatz; z.B. "3", "4a"
    """
    postfach: Optional[str] = None
    """Im Falle einer Postfachadresse das Postfach; Damit werden Straße und Hausnummer nicht berücksichtigt"""
    adresszusatz: Optional[str] = None
    """
    Zusatzhinweis zum Auffinden der Adresse, z.B. "3. Stock linke Wohnung"
    """
    co_ergaenzung: Optional[str] = None
    """
    Im Falle einer c/o-Adresse steht in diesem Attribut die Anrede. Z.B. "c/o Veronica Hauptmieterin"
    """
    landescode: Optional["Landescode"] = Landescode.DE  # type:ignore
    """Offizieller ISO-Landescode"""
