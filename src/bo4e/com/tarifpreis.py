"""
Contains Tarifpreis class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.preis import Preis
from bo4e.enum.preistyp import Preistyp


# pylint: disable=too-few-public-methods


class Tarifpreis(Preis):
    """
    Abbildung eines Tarifpreises mit Preistyp und Beschreibung abgeleitet von COM Preis.

    .. graphviz:: /api/dots/bo4e/com/Tarifpreis.dot

    """

    # required attributes
    #:  Angabe des Preistypes (z.B. Grundpreis)
    preistyp: Preistyp

    # optional attributes
    #:  Beschreibung des Preises. Hier können z.B. Preisdetails angegeben sein, beispielsweise "Drehstromzähler".
    beschreibung: str = None
