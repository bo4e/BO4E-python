"""
Contains Lokationszuordnung class
"""

from typing import Annotated, Optional

from pydantic import Field

from ..bo.marktlokation import Marktlokation
from ..bo.messlokation import Messlokation
from ..bo.netzlokation import Netzlokation
from ..bo.steuerbareressource import SteuerbareRessource
from ..bo.technischeressource import TechnischeRessource
from ..com.zeitspanne import Zeitspanne
from ..enum.typ import Typ
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt


@postprocess_docstring
class Lokationszuordnung(Geschaeftsobjekt):
    """
    Modell für die Abbildung der Referenz auf die Lokationsbündelstruktur. Diese gibt an welche Marktlokationen,
    Messlokationen, Netzlokationen, technische/steuerbaren Ressourcen an einer Lokation vorhanden sind;

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Lokationszuordnung.svg" type="image/svg+xml"></object>

    .. HINT::
        `Lokationszuordnung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Lokationszuordnung.json>`_
    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.LOKATIONSZUORDNUNG

    #: Liste mit referenzierten Marktlokationen
    marktlokationen: Optional[list[Marktlokation]] = None
    #: Liste mit referenzierten Messlokationen
    messlokationen: Optional[list[Messlokation]] = None
    #: Liste mit referenzierten Netzlokationen
    netzlokationen: Optional[list[Netzlokation]] = None
    #: Liste mit referenzierten technischen Ressourcen
    technische_ressourcen: Optional[list[TechnischeRessource]] = None
    #: Liste mit referenzierten steuerbaren Ressourcen
    steuerbare_ressourcen: Optional[list[SteuerbareRessource]] = None
    #: Zeitspanne der Gültigkeit
    gueltigkeit: Optional[Zeitspanne] = None
    #: Verknüpfungsrichtung z.B. Malo-Melo
    zuordnungstyp: Optional[str] = None
    #: Code, der angibt wie die Lokationsbündelstruktur zusammengesetzt ist (zu finden unter "Codeliste der Lokationsbündelstrukturen" auf https://www.edi-energy.de/index.php?id=38)
    lokationsbuendelcode: Optional[str] = None
