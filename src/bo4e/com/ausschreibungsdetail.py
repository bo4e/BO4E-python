"""
Contains class Ausschreibungsdetail and corresponding marshmallow schema for de-/serialization
"""

from typing import Optional

from pydantic import StrictStr, StrictBool

from bo4e.com.adresse import Adresse
from bo4e.com.com import COM
from bo4e.com.menge import Menge
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.zaehlertyp import Zaehlertyp


# pylint: disable=too-few-public-methods, too-many-instance-attributes


class Ausschreibungsdetail(COM):
    """
    Die Komponente Ausschreibungsdetail wird verwendet um die Informationen zu einer Abnahmestelle innerhalb eines
    Ausschreibungsloses abzubilden.

    .. HINT::
        `Ausschreibungsdetail JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AusschreibungsdetailSchema.json>`_

    """

    # required attributes
    #: Identifikation einer ausgeschriebenen Marktlokation
    lokations_id: str
    #: In der angegebenen Netzebene wird die Marktlokation versorgt, z.B. MSP für Mittelspannung
    netzebene_lieferung: str
    #: In der angegebenen Netzebene wird die Lokation gemessen, z.B. NSP für Niederspannung
    netzebene_messung: str
    #: Die Adresse an der die Marktlokation sich befindet
    lokationsadresse: Adresse
    #: Angefragter Zeitraum für die ausgeschriebene Belieferung
    lieferzeitraum: Zeitraum

    # optional attributes
    #: Bezeichnung des zuständigen Netzbetreibers, z.B. 'Stromnetz Hamburg GmbH'
    netzbetreiber: str = None
    #: Bezeichnung des Kunden, der die Marktlokation nutzt
    kunde: str = None
    #: Die Bezeichnung des Zählers an der Marktlokation
    zaehlernummer: str = None
    #: Bezeichnung für die Lokation, z.B. 'Zentraler Einkauf, Hamburg'
    lokationsbezeichnung: str = None

    #: Spezifikation, um welche Zählertechnik es sich im vorliegenden Fall handelt, z.B. Leistungsmessung
    zaehlertechnik: Zaehlertyp = None
    lastgang_vorhanden: bool = None
    """
    Zeigt an, ob es zu der Marktlokation einen Lastgang gibt.
    Falls ja, kann dieser abgerufen werden und daraus die Verbrauchswerte ermittelt werden
    """

    #: Prognosewert für die Jahresarbeit der ausgeschriebenen Lokation
    prognose_jahresarbeit: Menge = None
    #: Ein Prognosewert für die Arbeit innerhalb des angefragten Lieferzeitraums der ausgeschriebenen Lokation
    prognose_arbeit_lieferzeitraum: Menge = None
    #: Prognosewert für die abgenommene maximale Leistung der ausgeschriebenen Lokation
    prognose_leistung: Menge = None
    #: Die (evtl. abweichende) Rechnungsadresse
    rechnungsadresse: Adresse = None
