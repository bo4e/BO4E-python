"""
Contains class Ausschreibungsdetail and corresponding marshmallow schema for de-/serialization
"""

from typing import TYPE_CHECKING, Optional

from ..utils import postprocess_docstring
from .com import COM

if TYPE_CHECKING:
    from ..enum.zaehlertyp import Zaehlertyp
    from .adresse import Adresse
    from .menge import Menge
    from .zeitraum import Zeitraum

# pylint: disable=too-few-public-methods, too-many-instance-attributes


@postprocess_docstring
class Ausschreibungsdetail(COM):
    """
    Die Komponente Ausschreibungsdetail wird verwendet um die Informationen zu einer Abnahmestelle innerhalb eines
    Ausschreibungsloses abzubilden.

    .. raw:: html

        <object data="../_static/images/bo4e/com/Ausschreibungsdetail.svg" type="image/svg+xml"></object>

    .. HINT::
        `Ausschreibungsdetail JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/BO4E/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Ausschreibungsdetail.json>`_

    """

    marktlokations_id: Optional[str] = None
    """Identifikation einer ausgeschriebenen Marktlokation"""
    netzebene_lieferung: Optional[str] = None
    """In der angegebenen Netzebene wird die Marktlokation versorgt, z.B. MSP für Mittelspannung"""
    netzebene_messung: Optional[str] = None
    """In der angegebenen Netzebene wird die Lokation gemessen, z.B. NSP für Niederspannung"""
    marktlokationsadresse: Optional["Adresse"] = None
    """Die Adresse an der die Marktlokation sich befindet"""
    lieferzeitraum: Optional["Zeitraum"] = None
    """Angefragter Zeitraum für die ausgeschriebene Belieferung"""

    netzbetreiber: Optional[str] = None
    """Bezeichnung des zuständigen Netzbetreibers, z.B. 'Stromnetz Hamburg GmbH'"""
    kunde: Optional[str] = None
    """Bezeichnung des Kunden, der die Marktlokation nutzt"""
    zaehlernummer: Optional[str] = None
    """Die Bezeichnung des Zählers an der Marktlokation"""
    marktlokationsbezeichnung: Optional[str] = None
    """Bezeichnung für die Lokation, z.B. 'Zentraler Einkauf, Hamburg'"""

    zaehlertechnik: Optional["Zaehlertyp"] = None
    """Spezifikation, um welche Zählertechnik es sich im vorliegenden Fall handelt, z.B. Leistungsmessung"""
    ist_lastgang_vorhanden: Optional[bool] = None
    """
    Zeigt an, ob es zu der Marktlokation einen Lastgang gibt.
    Falls ja, kann dieser abgerufen werden und daraus die Verbrauchswerte ermittelt werden
    """

    prognose_jahresarbeit: Optional["Menge"] = None
    """Prognosewert für die Jahresarbeit der ausgeschriebenen Lokation"""
    prognose_arbeit_lieferzeitraum: Optional["Menge"] = None
    """Ein Prognosewert für die Arbeit innerhalb des angefragten Lieferzeitraums der ausgeschriebenen Lokation"""
    prognose_leistung: Optional["Menge"] = None
    """Prognosewert für die abgenommene maximale Leistung der ausgeschriebenen Lokation"""
    rechnungsadresse: Optional["Adresse"] = None
    """Die (evtl. abweichende) Rechnungsadresse"""
