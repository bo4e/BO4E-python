"""
Contains Produkt class
"""

from typing import TYPE_CHECKING, Annotated, Literal, Optional

from pydantic import Field

from ..enum.botyp import BoTyp
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt

if TYPE_CHECKING:
    from ..com.tarif import Tarif
    from ..com.vertragskonditionen import Vertragskonditionen
    from ..com.zeitraum import Zeitraum
    from ..enum.kundentyp import Kundentyp
    from ..enum.produkttyp import Produkttyp
    from ..enum.sparte import Sparte
    from .marktteilnehmer import Marktteilnehmer

# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
# pylint: disable=too-many-instance-attributes


@postprocess_docstring
class Produkt(Geschaeftsobjekt):
    """
    Modell für die Abbildung eines Produkts, z.B. eines Tarifprodukts.
    Ein Produkt bündelt die vermarktungsrelevanten Eigenschaften und referenziert
    den zugrundeliegenden Tarif.

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Produkt.svg" type="image/svg+xml"></object>

    .. HINT::
        `Produkt JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Produkt.json>`_

    """

    typ: Annotated[Literal[BoTyp.PRODUKT], Field(alias="_typ")] = BoTyp.PRODUKT

    bezeichnung: Optional[str] = None
    """Eine (beliebige) Bezeichnung für das Produkt."""
    beschreibung: Optional[str] = None
    """Eine (beliebige) Beschreibung für das Produkt."""
    produkttyp: Optional["Produkttyp"] = None
    """Die Art des Produkts, z.B. Tarifprodukt."""
    tarif: Optional["Tarif"] = None
    """Der dem Produkt zugrundeliegende Tarif."""
    sparte: Optional["Sparte"] = None
    """Strom / Gas"""
    anbieter: Optional["Marktteilnehmer"] = None
    """Der Marktteilnehmer, der dieses Produkt anbietet, angeboten hat oder anbieten wird."""
    zeitraum_vermarktung: Optional["Zeitraum"] = None
    """Der Zeitraum, in dem das Produkt beim Anbieter vertraglich abschließbar ist."""
    zeitraum_belieferbarkeit: Optional["Zeitraum"] = None
    """Der Zeitraum, in dem eine Belieferung (für dieses Produkt) möglich ist."""
    vertragskonditionen: Optional["Vertragskonditionen"] = None
    """
    Vertragskonditionen für dieses Produkt.
    Die Redundanz zu den Vertragskonditionen am Vertrag ist gewollt: die Konditionen
    des Produkts können bei der Vertragsausgestaltung überschrieben werden.
    """
    website: Optional[str] = None
    """Internetseite, auf der das Produkt veröffentlicht ist."""
    kundentypen: Optional[list["Kundentyp"]] = None
    """Eine Liste an Kundentypen, für die dieses Produkt vorgesehen ist."""
