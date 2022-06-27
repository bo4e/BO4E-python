"""
Contains StandorteigenschaftenAllgemein class
and corresponding marshmallow schema for de-/serialization
"""

from bo4e.com.com import COM


# pylint: disable=too-few-public-methods


class StandorteigenschaftenAllgemein(COM):
    """
    Allgemeine Standorteigenschaften

    .. graphviz:: /api/dots/bo4e/com/StandorteigenschaftenAllgemein.dot

    """

    # required attributes
    #: Die Postleitzahl des Standorts
    postleitzahl: str
    #: Die Ortsbezeichnung des Standorts
    ort: str
    #: Der Name des Kreises in dem der Standort liegt
    kreisname: str
    #: Der Name der Gemeinde des Standortes
    gemeindename: str
    #: Die standardisierte Kennziffer der Gemeinde
    gemeindekennziffer: str
    #: Anzahl der Einwohner in der Gemeinde
    gemeindeeinwohner: int
    #: Das Bundesland zu dem der Standort gehört
    bundesland: str
