"""
Contains PreisblattHardware class and corresponding marshmallow schema for de-/serialization
"""
from typing import List

from bo4e.bo.preisblatt import Preisblatt
from bo4e.com.geraeteeigenschaften import Geraeteeigenschaften
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.botyp import BoTyp
from bo4e.enum.dienstleistungstyp import Dienstleistungstyp
from bo4e.enum.netzebene import Netzebene


# pylint: disable=too-few-public-methods


class PreisblattHardware(Preisblatt):
    """
    Variante des Preisblattmodells zur Abbildung der Preise für zusätzliche Hardware

    .. HINT::
        `PreisblattHardware JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/PreisblattHardwareSchema.json>`_

    """

    bo_typ: BoTyp = BoTyp.PREISBLATTHARDWARE
    # required attributes (additional to those of Preisblatt)
    #: Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode
    bilanzierungsmethode: Bilanzierungsmethode
    #: Die Preise gelten für Messlokationen in der angebebenen Netzebene
    messebene: Netzebene

    #: Der Preis betriftt das hier angegebene Gerät, z.B. ein Tarifschaltgerät
    basisgeraet: Geraeteeigenschaften

    # optional attributes
    #: Im Preis sind die hier angegebenen Dienstleistungen enthalten, z.B. Jährliche Ablesung
    inklusive_dienstleistungen: List[Dienstleistungstyp] = None

    #: Im Preis sind die hier angegebenen Geräte mit enthalten, z.B. ein Wandler
    inklusive_geraete: List[Geraeteeigenschaften] = None
