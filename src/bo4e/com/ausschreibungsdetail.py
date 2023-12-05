"""
Contains class Ausschreibungsdetail and corresponding marshmallow schema for de-/serialization
"""
from typing import Optional

from ..enum.zaehlertyp import Zaehlertyp
from ..utils import postprocess_docstring
from .adresse import Adresse
from .com import COM
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
        `Ausschreibungsdetail JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/com/Ausschreibungsdetail.json>`_

    """

    #: Identifikation einer ausgeschriebenen Marktlokation
    marktlokations_id: Optional[str] = None
    #: In der angegebenen Netzebene wird die Marktlokation versorgt, z.B. MSP für Mittelspannung
    netzebene_lieferung: Optional[str] = None
    #: In der angegebenen Netzebene wird die Lokation gemessen, z.B. NSP für Niederspannung
    netzebene_messung: Optional[str] = None
    #: Die Adresse an der die Marktlokation sich befindet
    marktlokationsadresse: Optional[Adresse] = None
    #: Angefragter Zeitraum für die ausgeschriebene Belieferung
    lieferzeitraum: Optional[Zeitraum] = None

    #: Bezeichnung des zuständigen Netzbetreibers, z.B. 'Stromnetz Hamburg GmbH'
    netzbetreiber: Optional[str] = None
    #: Bezeichnung des Kunden, der die Marktlokation nutzt
    kunde: Optional[str] = None
    #: Die Bezeichnung des Zählers an der Marktlokation
    zaehlernummer: Optional[str] = None
    #: Bezeichnung für die Lokation, z.B. 'Zentraler Einkauf, Hamburg'
    marktlokationsbezeichnung: Optional[str] = None

    #: Spezifikation, um welche Zählertechnik es sich im vorliegenden Fall handelt, z.B. Leistungsmessung
    zaehlertechnik: Optional[Zaehlertyp] = None
    ist_lastgang_vorhanden: Optional[bool] = None
    """
    Zeigt an, ob es zu der Marktlokation einen Lastgang gibt.
    Falls ja, kann dieser abgerufen werden und daraus die Verbrauchswerte ermittelt werden
    """

    #: Prognosewert für die Jahresarbeit der ausgeschriebenen Lokation
    prognose_jahresarbeit: Optional[Menge] = None
    #: Ein Prognosewert für die Arbeit innerhalb des angefragten Lieferzeitraums der ausgeschriebenen Lokation
    prognose_arbeit_lieferzeitraum: Optional[Menge] = None
    #: Prognosewert für die abgenommene maximale Leistung der ausgeschriebenen Lokation
    prognose_leistung: Optional[Menge] = None
    #: Die (evtl. abweichende) Rechnungsadresse
    rechnungsadresse: Optional[Adresse] = None
