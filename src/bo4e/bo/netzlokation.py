"""
Contains Netzlokation class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Annotated, Optional

from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.konfigurationsprodukt import Konfigurationsprodukt
    from ..com.menge import Menge
    from ..com.verwendungszweckpromarktrolle import VerwendungszweckProMarktrolle
    from ..enum.marktrolle import Marktrolle
    from ..enum.sparte import Sparte


# pylint: disable=too-many-instance-attributes, too-few-public-methods


@postprocess_docstring
class Netzlokation(Geschaeftsobjekt):
    """
    Object containing information about a Netzlokation

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Netzlokation.svg" type="image/svg+xml"></object>

    .. HINT::
        `Netzlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Netzlokation.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.NETZLOKATION

    #: Identifikationsnummer einer Netzlokation, an der Energie entweder verbraucht, oder erzeugt wird
    netzlokations_id: Optional[str] = None
    #: Sparte der Netzlokation, z.B. Gas oder Strom.
    sparte: Optional["Sparte"] = None
    #: Netzanschlussleistungsmenge der Netzlokation
    netzanschlussleistung: Optional["Menge"] = None
    #: Codenummer des grundzuständigen Messstellenbetreibers, der für diese Netzlokation zuständig ist.
    grundzustaendiger_msb_codenr: Optional[str] = None
    #: Ob ein Steuerkanal der Netzlokation zugeordnet ist und somit die Netzlokation gesteuert werden kann.
    steuerkanal: Optional[bool] = None
    #: Die OBIS-Kennzahl für die Netzlokation
    obiskennzahl: Optional[str] = None
    #: Verwendungungszweck der Werte Netzlokation
    verwendungszweck: Optional["VerwendungszweckProMarktrolle"] = None
    #: Produkt-Daten der Netzlokation
    konfigurationsprodukte: Optional[list["Konfigurationsprodukt"]] = None
    #: Eigenschaft des Messstellenbetreibers an der Lokation
    eigenschaft_msb_lokation: Optional["Marktrolle"] = None
    #: Lokationsbuendel Code, der die Funktion dieses BOs an der Lokationsbuendelstruktur beschreibt.
    lokationsbuendel_objektcode: Optional[str] = None
