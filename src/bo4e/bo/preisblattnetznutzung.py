"""
Contains PreisblattNetnutzung class and corresponding marshmallow schema for de-/serialization
"""


from bo4e.bo.preisblatt import Preisblatt
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.botyp import BoTyp
from bo4e.enum.kundengruppe import Kundengruppe
from bo4e.enum.netzebene import Netzebene


# pylint: disable=too-few-public-methods


class PreisblattNetznutzung(Preisblatt):
    """
    Die Variante des Preisblattmodells zur Abbildung der Netznutzungspreise

    .. graphviz:: /api/dots/bo4e/bo/PreisblattNetznutzung.dot

    """

    bo_typ: BoTyp = BoTyp.PREISBLATTNETZNUTZUNG
    # required attributes (additional to those of Preisblatt)
    #: Die Preise gelten für Marktlokationen der angebebenen Bilanzierungsmethode
    bilanzierungsmethode: Bilanzierungsmethode
    #: Die Preise gelten für Marktlokationen in der angebebenen Netzebene
    netzebene: Netzebene
    kundengruppe: Kundengruppe

    # there are no optional attributes (additionally to those of Preisblatt)
