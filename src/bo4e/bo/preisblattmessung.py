"""
Contains PreisblattMessung class and corresponding marshmallow schema for de-/serialization
"""
from typing import List

from bo4e.bo.preisblatt import Preisblatt
from bo4e.com.geraeteeigenschaften import Geraeteeigenschaften
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.botyp import BoTyp
from bo4e.enum.dienstleistungstyp import Dienstleistungstyp
from bo4e.enum.netzebene import Netzebene


# pylint: disable=too-few-public-methods


class PreisblattMessung(Preisblatt):
    """
    Variante des Preisblattmodells zur Abbildung der Preise des Messstellenbetriebs und damit verbundener Leistungen

    .. graphviz:: /api/dots/bo4e/bo/PreisblattMessung.dot

    """

    bo_typ: BoTyp = BoTyp.PREISBLATTMESSUNG
    # required attributes (additional to those of Preisblatt)
    #: Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode
    bilanzierungsmethode: Bilanzierungsmethode
    #: Die Preise gelten für Messlokationen in der angebebenen Netzebene
    messebene: Netzebene

    #: Der Preis betrifft den hier angegebenen Zähler, z.B. einen Drehstromzähler
    zaehler: Geraeteeigenschaften
    # todo: https://github.com/Hochfrequenz/BO4E-python/issues/333

    # optional attributes
    #: Im Preis sind die hier angegebenen Dienstleistungen enthalten, z.B. Jährliche Ablesung
    inklusive_dienstleistungen: List[Dienstleistungstyp] = None

    #: Im Preis sind die hier angegebenen Geräte mit enthalten, z.B. ein Wandler
    inklusive_geraete: List[Geraeteeigenschaften] = None
