"""
Contains Marktteilnehmer class
and corresponding marshmallow schema for de-/serialization
"""


# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from typing import Optional

from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.enum.botyp import BoTyp
from bo4e.enum.marktrolle import Marktrolle
from bo4e.enum.rollencodetyp import Rollencodetyp
from bo4e.enum.sparte import Sparte


class Marktteilnehmer(Geschaeftspartner):
    """
    Objekt zur Aufnahme der Information zu einem Marktteilnehmer

    .. raw:: html

        <object data="../_static/images/bo4e/bo/Marktteilnehmer.svg" type="image/svg+xml"></object>

    .. HINT::
        `Marktteilnehmer JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/Marktteilnehmer.json>`_

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.MARKTTEILNEHMER
    #: Gibt im Klartext die Bezeichnung der Marktrolle an
    marktrolle: Optional[Marktrolle] = None
    #: Gibt die Codenummer der Marktrolle an
    rollencodenummer: Optional[str] = None
    #: Gibt den Typ des Codes an
    rollencodetyp: Optional[Rollencodetyp] = None
    #: Sparte des Marktteilnehmers, z.B. Gas oder Strom
    sparte: Optional[Sparte] = None

    # optional attributes
    #: Die 1:1-Kommunikationsadresse des Marktteilnehmers; Diese wird in der Marktkommunikation verwendet.
    makoadresse: Optional[str] = None
