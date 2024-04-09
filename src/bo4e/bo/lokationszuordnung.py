"""
Contains Lokationszuordnung class
"""

from typing import Annotated, Optional

from pydantic import Field

from ..com.zeitspanne import Zeitspanne
from ..enum.arithmetische_operation import ArithmetischeOperation
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

    #: Liste mit IDs der referenzierten Marktlokationen
    marktlokationen: Optional[list[str]] = None
    #: Liste mit IDs der referenzierten Messlokationen
    messlokationen: Optional[list[str]] = None
    #: Liste mit IDs der referenzierten Netzlokationen
    netzlokationen: Optional[list[str]] = None
    #: Liste mit IDs der referenzierten technischen Ressourcen
    technische_ressourcen: Optional[list[str]] = None
    #: Liste mit IDs der referenzierten steuerbaren Ressourcen
    steuerbare_ressourcen: Optional[list[str]] = None
    #: Zeitspanne der Gültigkeit
    gueltigkeit: Optional[Zeitspanne] = None
    #: Angabe einer arithmetischen Operation
    arithmetik: Optional[ArithmetischeOperation] = None
    #: Code, der angibt wie die Lokationsbündelstruktur zusammengesetzt ist
    zuordnungstyp: Optional[str] = None
