"""
Contains Tarifinfo class
and corresponding marshmallow schema for de-/serialization
"""
from typing import List, Optional


from bo4e.bo.geschaeftsobjekt import Geschaeftsobjekt
from bo4e.bo.marktteilnehmer import Marktteilnehmer
from bo4e.com.energiemix import Energiemix
from bo4e.com.vertragskonditionen import Vertragskonditionen
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.botyp import BoTyp
from bo4e.enum.kundentyp import Kundentyp
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.tarifmerkmal import Tarifmerkmal
from bo4e.enum.tariftyp import Tariftyp


# pylint: disable=too-many-instance-attributes, too-few-public-methods
from pydantic import conlist, StrictStr


class Tarifinfo(Geschaeftsobjekt):
    """
    Das BO Tarifinfo liefert die Merkmale, die einen Endkundentarif identifizierbar machen.
    Dieses BO dient als Basis für weitere BOs mit erweiterten Anwendungsmöglichkeiten.

    .. HINT::
        `Tarifinfo JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/TarifinfoSchema.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.TARIFINFO
    #: Name des Tarifs
    bezeichnung: str
    #: Der Name des Marktpartners, der den Tarif anbietet
    anbietername: str
    #: Strom oder Gas, etc.
    sparte: Sparte
    #: Kundentypen für den der Tarif gilt, z.B. Privatkunden
    kundentypen: conlist(Kundentyp, min_items=1)
    #: Die Art des Tarifes, z.B. Eintarif oder Mehrtarif
    tarifart: Tarifart
    #: Hinweis auf den Tariftyp, z.B. Grundversorgung oder Sondertarif
    tariftyp: Tariftyp
    #: Weitere Merkmale des Tarifs, z.B. Festpreis oder Vorkasse
    tarifmerkmale: conlist(Tarifmerkmal, min_items=1)
    #: Der Marktteilnehmer (Lieferant), der diesen Tarif anbietet
    anbieter: Marktteilnehmer

    # optional attributes
    #: Internetseite auf dem der Tarif zu finden ist
    website: str = None
    #: Freitext
    bemerkung: str = None

    #: Angabe, in welchem Zeitraum der Tarif gültig ist
    zeitliche_gueltigkeit: Zeitraum = None
    #: Der Energiemix, der für diesen Tarif gilt
    energiemix: Energiemix = None
    #: Mindestlaufzeiten und Kündigungsfristen zusammengefasst
    vertragskonditionen: Vertragskonditionen = None
