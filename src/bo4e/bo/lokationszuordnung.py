"""
Contains Lokationszuordnung class
"""

from typing import Annotated, Optional

from pydantic import Field

from ..bo.marktlokation import Marktlokation
from ..bo.messlokation import Messlokation
from ..bo.netzlokation import Netzlokation
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
    technische_ressourcen: Optional[list[str]] = None
    #: Liste mit referenzierten steuerbaren Ressourcen
    steuerbare_ressourcen: Optional[list[str]] = None
    #: Zeitspanne der Gültigkeit
    gueltigkeit: Optional[Zeitspanne] = None
    #:
    zuordnungstyp: Optional[str] = None
    #: Code, der angibt wie die Lokationsbündelstruktur zusammengesetzt ist (evtl. TODO: Enum erstellen für alle Fälle der Codeliste)
    lokationsbuendelcode: Optional[str] = None
