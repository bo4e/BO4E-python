"""
Contains PreisblattDienstleistung class and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional

from bo4e.bo.preisblatt import Preisblatt
from bo4e.com.geraeteeigenschaften import Geraeteeigenschaften
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.botyp import BoTyp
from bo4e.enum.dienstleistungstyp import Dienstleistungstyp

# pylint: disable=too-few-public-methods


class PreisblattDienstleistung(Preisblatt):
    """
    Variante des Preisblattmodells zur Abbildung der Preise für wahlfreie Dienstleistungen

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattDienstleistung.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattDienstleistung JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/PreisblattDienstleistung.json>`_

    """

    bo_typ: BoTyp = BoTyp.PREISBLATTDIENSTLEISTUNG
    # required attributes (additional to those of Preisblatt)
    #: Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode
    bilanzierungsmethode: Bilanzierungsmethode
    #: Dienstleistung, für die der Preis abgebildet wird, z.B. Sperrung/Entsperrung
    basisdienstleistung: Dienstleistungstyp

    # optional attributes
    #: Hier kann der Preis auf bestimmte Geräte eingegrenzt werden. Z.B. auf die Zählergröße
    geraetedetails: Optional[Geraeteeigenschaften] = None

    #: Weitere Dienstleistungen, die im Preis enthalten sind
    inklusive_dienstleistungen: Optional[List[Dienstleistungstyp]] = None
