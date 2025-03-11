"""
Contains Lokationszuordnung class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..bo.marktlokation import Marktlokation
    from ..bo.messlokation import Messlokation
    from ..bo.netzlokation import Netzlokation
    from ..bo.steuerbareressource import SteuerbareRessource
    from ..bo.technischeressource import TechnischeRessource
    from ..com.zeitspanne import Zeitspanne


@postprocess_docstring
class Lokationszuordnung(Geschaeftsobjekt):
    """
    Modell für die Abbildung der Referenz auf die Lokationsbündelstruktur. Diese gibt an welche Marktlokationen,
    Messlokationen, Netzlokationen, technische/steuerbaren Ressourcen an einer Lokation vorhanden sind.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Lokationszuordnung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Lokationszuordnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Lokationszuordnung.json>`_
    """

    typ: Annotated[Literal[Typ.LOKATIONSZUORDNUNG], Field(alias="_typ")] = Typ.LOKATIONSZUORDNUNG

    marktlokationen: Optional[list["Marktlokation"]] = None
    """Liste mit referenzierten Marktlokationen"""
    messlokationen: Optional[list["Messlokation"]] = None
    """Liste mit referenzierten Messlokationen"""
    netzlokationen: Optional[list["Netzlokation"]] = None
    """Liste mit referenzierten Netzlokationen"""
    technische_ressourcen: Optional[list["TechnischeRessource"]] = None
    """Liste mit referenzierten technischen Ressourcen"""
    steuerbare_ressourcen: Optional[list["SteuerbareRessource"]] = None
    """Liste mit referenzierten steuerbaren Ressourcen"""
    gueltigkeit: Optional["Zeitspanne"] = None
    """Zeitspanne der Gültigkeit"""
    zuordnungstyp: Optional[str] = None
    """Verknüpfungsrichtung z.B. Malo-Melo [TODO: Eventuell anderer Datentyp]"""
    lokationsbuendelcode: Optional[str] = None
    """Code, der angibt wie die Lokationsbündelstruktur zusammengesetzt ist (zu finden unter "Codeliste der Lokationsbündelstrukturen" auf https://www.edi-energy.de/index.php?id=38)"""
