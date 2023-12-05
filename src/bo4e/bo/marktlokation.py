"""
Contains Marktlokation class
and corresponding marshmallow schema for de-/serialization
"""

# pylint: disable=too-many-instance-attributes, too-few-public-methods
from typing import Annotated, Optional

from pydantic import Field

from ..com.adresse import Adresse
from ..com.geokoordinaten import Geokoordinaten
from ..com.katasteradresse import Katasteradresse
from ..com.messlokationszuordnung import Messlokationszuordnung
from ..enum.bilanzierungsmethode import Bilanzierungsmethode
from ..enum.energierichtung import Energierichtung
from ..enum.gasqualitaet import Gasqualitaet
from ..enum.gebiettyp import Gebiettyp
from ..enum.kundentyp import Kundentyp
from ..enum.netzebene import Netzebene
from ..enum.sparte import Sparte
from ..enum.typ import Typ
from ..enum.verbrauchsart import Verbrauchsart
from ..utils import postprocess_docstring
from .geschaeftsobjekt import Geschaeftsobjekt
from .geschaeftspartner import Geschaeftspartner

# pylint: disable=no-name-in-module


@postprocess_docstring
class Marktlokation(Geschaeftsobjekt):
    """
    Object containing information about a Marktlokation

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Marktlokation.svg" type="image/svg+xml"></object>

    .. HINT::
        `Marktlokation JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-Schemas/{__gh_version__}/src/bo4e_schemas/bo/Marktlokation.json>`_

    """

    typ: Annotated[Optional[Typ], Field(alias="_typ")] = Typ.MARKTLOKATION
    #: Identifikationsnummer einer Marktlokation, an der Energie entweder verbraucht, oder erzeugt wird.
    marktlokations_id: Optional[str] = None
    #: Sparte der Marktlokation, z.B. Gas oder Strom
    sparte: Optional[Sparte] = None
    #: Kennzeichnung, ob Energie eingespeist oder entnommen (ausgespeist) wird
    energierichtung: Optional[Energierichtung] = None
    #: Die Bilanzierungsmethode, RLM oder SLP
    bilanzierungsmethode: Optional[Bilanzierungsmethode] = None
    netzebene: Optional[Netzebene] = None
    """
    Netzebene, in der der Bezug der Energie erfolgt.
    Bei Strom Spannungsebene der Lieferung, bei Gas Druckstufe.
    Beispiel Strom: Niederspannung Beispiel Gas: Niederdruck.
    """

    #: Verbrauchsart der Marktlokation.
    verbrauchsart: Optional[Verbrauchsart] = None
    #: Gibt an, ob es sich um eine unterbrechbare Belieferung handelt
    ist_unterbrechbar: Optional[bool] = None
    #: Codenummer des Netzbetreibers, an dessen Netz diese Marktlokation angeschlossen ist.
    netzbetreibercodenr: Optional[str] = None
    #: Typ des Netzgebietes, z.B. Verteilnetz
    gebietstyp: Optional[Gebiettyp] = None
    #: Die ID des Gebietes in der ene't-Datenbank
    netzgebietsnr: Optional[str] = None  # todo: rename to "id" (see 2021-12-15 update)
    #: Bilanzierungsgebiet, dem das Netzgebiet zugeordnet ist - im Falle eines Strom Netzes
    bilanzierungsgebiet: Optional[str] = None
    #: Codenummer des Grundversorgers, der für diese Marktlokation zuständig ist
    grundversorgercodenr: Optional[str] = None
    #: Die Gasqualität in diesem Netzgebiet. H-Gas oder L-Gas. Im Falle eines Gas-Netzes
    gasqualitaet: Optional[Gasqualitaet] = None
    #: Geschäftspartner, dem diese Marktlokation gehört
    endkunde: Optional[Geschaeftspartner] = None
    zugehoerige_messlokation: Optional[Messlokationszuordnung] = None  # todo: rename to plural
    """
    Aufzählung der Messlokationen, die zu dieser Marktlokation gehören.
    Es können 3 verschiedene Konstrukte auftreten:

    Beziehung 1 : 0 : Hier handelt es sich um Pauschalanlagen ohne Messung. D.h. die Verbrauchsdaten sind direkt über
    die Marktlokation abgreifbar.
    Beziehung 1 : 1 : Das ist die Standard-Beziehung für die meisten Fälle. In diesem Fall gibt es zu einer
    Marktlokation genau eine Messlokation.
    Beziehung 1 : N : Hier liegt beispielsweise eine Untermessung vor. Der Verbrauch einer Marklokation berechnet sich
    hier aus mehreren Messungen.

    Es gibt praktisch auch noch die Beziehung N : 1, beispielsweise bei einer Zweirichtungsmessung bei der durch eine
    Messeinrichtung die Messung sowohl für die Einspreiseseite als auch für die Aussspeiseseite erfolgt.
    Da Abrechnung und Bilanzierung jedoch für beide Marktlokationen getrennt erfolgt, werden nie beide Marktlokationen
    gemeinsam betrachtet. Daher lässt sich dieses Konstrukt auf zwei 1:1-Beziehung zurückführen,
    wobei die Messlokation in beiden Fällen die gleiche ist.

    In den Zuordnungen sind ist die arithmetische Operation mit der der Verbrauch einer Messlokation zum Verbrauch einer
    Marktlokation beitrögt mit aufgeführt.
    Der Standard ist hier die Addition.
    """

    # only one of the following three optional attributes can be set
    #: Die Adresse, an der die Energie-Lieferung oder -Einspeisung erfolgt
    lokationsadresse: Optional[Adresse] = None
    geoadresse: Optional[Geokoordinaten] = None
    """
    Alternativ zu einer postalischen Adresse kann hier ein Ort mittels Geokoordinaten angegeben werden
    (z.B. zur Identifikation von Sendemasten).
    """
    katasterinformation: Optional[Katasteradresse] = None
    """
    Alternativ zu einer postalischen Adresse und Geokoordinaten kann hier eine Ortsangabe mittels Gemarkung und
    Flurstück erfolgen.
    """

    kundengruppen: Optional[list[Kundentyp]] = None
    #: Kundengruppen der Marktlokation
