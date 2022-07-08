"""
Contains PreisblattKonzessionsabgabe class and corresponding marshmallow schema for de-/serialization
"""


from bo4e.bo.preisblatt import Preisblatt
from bo4e.enum.botyp import BoTyp
from bo4e.enum.kundengruppeka import KundengruppeKA

# pylint: disable=too-few-public-methods


class PreisblattKonzessionsabgabe(Preisblatt):
    """
    Die Variante des Preisblattmodells zur Abbildung von allgemeinen Abgaben

    .. raw:: html

        <object data="../_static/images/bo4e/bo/PreisblattKonzessionsabgabe.svg" type="image/svg+xml"></object>

    .. HINT::
        `PreisblattKonzessionsabgabe JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/PreisblattKonzessionsabgabe.json>`_

    """

    bo_typ: BoTyp = BoTyp.PREISBLATTKONZESSIONSABGABE
    # required attributes (additional to those of Preisblatt)
    #: Kundegruppe anhand derer die Höhe der Konzessionabgabe festgelegt ist
    kundengruppe_k_a: KundengruppeKA

    # there are no optional attributes (additionally to those of Preisblatt)
