# pylint:disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum


class BoTyp(StrEnum):
    """
    Auflistung sämtlicher existierender Geschäftsobjekte.
    """

    ANGEBOT = "ANGEBOT"
    ANSPRECHPARTNER = "ANSPRECHPARTNER"
    AUSSCHREIBUNG = "AUSSCHREIUNG"
    AVIS = "AVIS"
    BUENDELVERTRAG = "BUENDELVERTRAG"
    ENERGIEMENGE = "ENERGIEMENGE"
    FREMDKOSTEN = "FREMDKOSTEN"
    # It is practical to use the BoTyp Enum as discriminator in the database.
    # Therefore, we added one additional entry for GESCHAEFTSOBJEKT
    # This is not defined by the documentation!
    GESCHAEFTSOBJEKT = "GESCHAEFTSOBJEKT"
    GESCHAEFTSPARTNER = "GESCHAEFTSPARTNER"
    KOSTEN = "KOSTEN"
    LASTGANG = "LASTGANG"
    LASTGANG_KOMPAKT = "LASTGANG_KOMPAKT"
    MARKTLOKATION = "MARKTLOKATION"
    MESSLOKATION = "MESSLOKATION"
    MARKTTEILNEHMER = "MARKTTEILNEHMER"
    NETZNUTZUNGSRECHNUNG = "NETZNUTZUNGSRECHNUNG"
    PREISBLATT = "PREISBLATT"
    PREISBLATTDIENSTLEISTUNG = "PREISBLATTDIENSTLEISTUNG"
    PREISBLATTHARDWARE = "PREISBLATTHARDWARE"
    PREISBLATTKONZESSIONSABGABE = "PREISBLATTKONZESSIONSABGABE"
    PREISBLATTMESSUNG = "PREISBLATTMESSUNG"
    PREISBLATTNETZNUTZUNG = "PREISBLATTNETZNUTZUNG"
    PREISBLATTUMLAGEN = "PREISBLATTUMLAGEN"
    RECHNUNG = "RECHNUNG"
    REGION = "REGION"
    REGIONALTARIF = "REGIONALTARIF"
    STANDORTEIGENSCHAFTEN = "STANDORTEIGENSCHAFTEN"
    TARIF = "TARIF"
    TARIFINFO = "TARIFINFO"
    TARIFKOSTEN = "TARIFKOSTEN"
    TARIFPREISBLATT = "TARIFPREISBLATT"
    VERTRAG = "VERTRAG"
    ZAEHLER = "ZAEHLER"
    ZEITREIHE = "ZEITREIHE"
