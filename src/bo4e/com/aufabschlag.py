"""
Contains AufAbschlag class
and corresponding marshmallow schema for de-/serialization
"""

from typing import List, Optional


from pydantic import validator, StrictStr

from bo4e.com.com import COM
from bo4e.com.preisstaffel import Preisstaffel
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.aufabschlagstyp import AufAbschlagstyp
from bo4e.enum.aufabschlagsziel import AufAbschlagsziel
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from bo4e.validators import einheit_only_for_abschlagstyp_absolut


# pylint: disable=too-few-public-methods, too-many-instance-attributes


class AufAbschlag(COM):
    """
    Modell für die preiserhöhenden (Aufschlag) bzw. preisvermindernden (Abschlag) Zusatzvereinbarungen,
    die individuell zu einem neuen oder bestehenden Liefervertrag abgeschlossen wurden.

    .. HINT::
        `AufAbschlag JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/com/AufAbschlagSchema.json>`_

    """

    # required attributes
    #: Bezeichnung des Auf-/Abschlags
    bezeichnung: str
    #: Werte für die gestaffelten Auf/Abschläge.
    staffeln: List[Preisstaffel]

    # optional attributes
    #: Beschreibung zum Auf-/Abschlag
    beschreibung: str = None
    #: Typ des Aufabschlages (z.B. absolut oder prozentual).
    auf_abschlagstyp: AufAbschlagstyp = None
    #: Diesem Preis oder den Kosten ist der Auf/Abschlag zugeordnet. Z.B. Arbeitspreis, Gesamtpreis etc..
    auf_abschlagsziel: AufAbschlagsziel = None
    einheit: Waehrungseinheit = None
    _einheit_check = validator("einheit", allow_reuse=True)(einheit_only_for_abschlagstyp_absolut)
    """ Gibt an in welcher Währungseinheit der Auf/Abschlag berechnet wird. Euro oder Ct..
    (Nur im Falle absoluter Aufschlagstypen). """
    #: Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind.
    website: str = None
    #: Internetseite, auf der die Informationen zum Auf-/Abschlag veröffentlicht sind.
    gueltigkeitszeitraum: Zeitraum = None
