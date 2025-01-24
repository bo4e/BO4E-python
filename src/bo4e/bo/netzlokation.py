"""
Contains Netzlokation class
and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..bo.lokationszuordnung import Lokationszuordnung
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

    typ: Annotated[Literal[Typ.NETZLOKATION], Field(alias="_typ")] = Typ.NETZLOKATION

    netzlokations_id: Optional[str] = None
    """Identifikationsnummer einer Netzlokation, an der Energie entweder verbraucht, oder erzeugt wird"""
    sparte: Optional["Sparte"] = None
    """Sparte der Netzlokation, z.B. Gas oder Strom."""
    netzanschlussleistung: Optional["Menge"] = None
    """Netzanschlussleistungsmenge der Netzlokation"""
    grundzustaendiger_msb_codenr: Optional[str] = None
    """Codenummer des grundzuständigen Messstellenbetreibers, der für diese Netzlokation zuständig ist."""
    steuerkanal: Optional[bool] = None
    """Ob ein Steuerkanal der Netzlokation zugeordnet ist und somit die Netzlokation gesteuert werden kann."""
    obiskennzahl: Optional[str] = None
    """Die OBIS-Kennzahl für die Netzlokation"""
    verwendungszweck: Optional["VerwendungszweckProMarktrolle"] = None
    """Verwendungungszweck der Werte Netzlokation"""
    konfigurationsprodukte: Optional[list["Konfigurationsprodukt"]] = None
    """Produkt-Daten der Netzlokation"""
    eigenschaft_msb_lokation: Optional["Marktrolle"] = None
    """Eigenschaft des Messstellenbetreibers an der Lokation"""
    lokationszuordnungen: Optional[list["Lokationszuordnung"]] = None
    """Lokationszuordnung, um bspw. die zugehörigen Messlokationen anzugeben"""
    lokationsbuendel_objektcode: Optional[str] = None
    """Lokationsbuendel Code, der die Funktion dieses BOs an der Lokationsbuendelstruktur beschreibt."""
