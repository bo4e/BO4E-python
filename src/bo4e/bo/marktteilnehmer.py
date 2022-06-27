"""
Contains Marktteilnehmer class
and corresponding marshmallow schema for de-/serialization
"""


# pylint: disable=too-few-public-methods
# pylint: disable=no-name-in-module
from pydantic import constr

from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.enum.botyp import BoTyp
from bo4e.enum.marktrolle import Marktrolle
from bo4e.enum.rollencodetyp import Rollencodetyp


class Marktteilnehmer(Geschaeftspartner):
    """
    Objekt zur Aufnahme der Information zu einem Marktteilnehmer

    .. graphviz:: /api/dots/bo4e/bo/Marktteilnehmer.dot

    """

    # required attributes
    bo_typ: BoTyp = BoTyp.MARKTTEILNEHMER
    #: Gibt im Klartext die Bezeichnung der Marktrolle an
    marktrolle: Marktrolle
    #: Gibt die Codenummer der Marktrolle an
    rollencodenummer: constr(strict=True, regex=r"^\d{13}$")
    #: Gibt den Typ des Codes an
    rollencodetyp: Rollencodetyp

    # optional attributes
    #: Die 1:1-Kommunikationsadresse des Marktteilnehmers; Diese wird in der Marktkommunikation verwendet.
    makoadresse: str = None
