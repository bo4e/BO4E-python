# pylint:disable=missing-module-docstring

from bo4e.enum.strenum import StrEnum


# pylint: disable=line-too-long
class Dienstleistungstyp(StrEnum):
    """
    Auflistung möglicher abzurechnender Dienstleistungen.
    """

    DATENBEREITSTELLUNG_TAEGLICH = "DATENBEREITSTELLUNG_TAEGLICH"  #: Datenbereitstellung täglich
    DATENBEREITSTELLUNG_WOECHENTLICH = "DATENBEREITSTELLUNG_WOECHENTLICH"  #: Datenbereitstellung wöchentlich
    DATENBEREITSTELLUNG_MONATLICH = "DATENBEREITSTELLUNG_MONATLICH"  #: Datenbereitstellung monatlich
    DATENBEREITSTELLUNG_JAEHRLICH = "DATENBEREITSTELLUNG_JAEHRLICH"  #: Datenbereitstellung jährlich
    DATENBEREITSTELLUNG_HISTORISCHE_LG = "DATENBEREITSTELLUNG_HISTORISCHE_LG"
    # Datenbereitstellung historischer Lastgänge
    DATENBEREITSTELLUNG_STUENDLICH = "DATENBEREITSTELLUNG_STUENDLICH"  #: Datenbereitstellung stündlich
    DATENBEREITSTELLUNG_VIERTELJAEHRLICH = "DATENBEREITSTELLUNG_VIERTELJAEHRLICH"
    # Datenbereitstellung vierteljährlich
    DATENBEREITSTELLUNG_HALBJAEHRLICH = "DATENBEREITSTELLUNG_HALBJAEHRLICH"  #: Datenbereitstellung halbjährlich
    DATENBEREITSTELLUNG_MONATLICH_ZUSAETZLICH = "DATENBEREITSTELLUNG_MONATLICH_ZUSAETZLICH"
    # Datenbereitstellung monatlich zusätzlich
    DATENBEREITSTELLUNG_EINMALIG = "DATENBEREITSTELLUNG_EINMALIG"  #: Datenbereitstellung einmalig
    AUSLESUNG_2X_TAEGLICH_FERNAUSLESUNG = "AUSLESUNG_2X_TAEGLICH_FERNAUSLESUNG"
    # Auslesung 2x täglich mittels Fernauslesung
    AUSLESUNG_TAEGLICH_FERNAUSLESUNG = "AUSLESUNG_TAEGLICH_FERNAUSLESUNG"  #: Auslesung täglich mittels Fernauslesung
    AUSLESUNG_MANUELL_MSB = "AUSLESUNG_MANUELL_MSB"  #: Auslesung, manuell vom Messstellenbetreiber vorgenommen
    AUSLESUNG_MONATLICH_FERNAUSLESUNG = "AUSLESUNG_MONATLICH_FERNAUSLESUNG"
    # Auslesung monatlich bei mittels Fernauslesung
    AUSLESUNG_JAEHRLICH_FERNAUSLESUNG = "AUSLESUNG_JAEHRLICH_FERNAUSLESUNG"
    # Auslesung jährlich bei SLP mittels Fernauslesung
    AUSLESUNG_MDE = "AUSLESUNG_MDE"  #: Auslesung mit mobiler Daten Erfassung (MDE)
    ABLESUNG_MONATLICH = "ABLESUNG_MONATLICH"  #: Ablesung monatlich
    ABLESUNG_VIERTELJAEHRLICH = "ABLESUNG_VIERTELJAEHRLICH"  #: Ablesung vierteljährlich
    ABLESUNG_HALBJAEHRLICH = "ABLESUNG_HALBJAEHRLICH"  #: Ablesung halbjährlich
    ABLESUNG_JAEHRLICH = "ABLESUNG_JAEHRLICH"  #: Ablesung jährlich
    AUSLESUNG_FERNAUSLESUNG = "AUSLESUNG_FERNAUSLESUNG"  #: Auslesung mittels Fernauslesung
    ABLESUNG_ZUSAETZLICH_MSB = "ABLESUNG_ZUSAETZLICH_MSB"  #: Ablesung, zusätzlich vom Messstellenbetreiber vorgenommen
    ABLESUNG_ZUSAETZLICH_KUNDE = "ABLESUNG_ZUSAETZLICH_KUNDE"  #: Ablesung SLP, zusätzlich vom Kunden vorgenommen
    AUSLESUNG_FERNAUSLESUNG_ZUSAETZLICH_MSB = "AUSLESUNG_FERNAUSLESUNG_ZUSAETZLICH_MSB"
    # Auslesung, mittels Fernauslesung, zusätzlich vom Messstellenbetreiber vorgenommen
    AUSLESUNG_MOATLICH_FERNAUSLESUNG = "AUSLESUNG_MOATLICH_FERNAUSLESUNG"  #: Auslesung monatlich mittels Fernauslesung
    AUSLESUNG_STUENDLICH_FERNAUSLESUNG = "AUSLESUNG_STUENDLICH_FERNAUSLESUNG"
    # Auslesung stündlich mittels Fernauslesung
    AUSLESUNG_TEMPERATURMENGENUMWERTER = "AUSLESUNG_TEMPERATURMENGENUMWERTER"  #: Auslesung Temperaturmengenumwerter
    AUSLESUNG_ZUSTANDSMENGENUMWERTER = "AUSLESUNG_ZUSTANDSMENGENUMWERTER"  #: Auslesung Zustandsmengenumwerter
    AUSLESUNG_SYSTEMMENGENUMWERTER = "AUSLESUNG_SYSTEMMENGENUMWERTER"  #: Auslesung Systemmengenumwerter
    AUSLESUNG_VORGANG = "AUSLESUNG_VORGANG"  #: Auslesung je Vorgang
    AUSLESUNG_KOMPAKTMENGENUMWERTER = "AUSLESUNG_KOMPAKTMENGENUMWERTER"  #: Auslesung Kompaktmengenumwerter
    SPERRUNG = "SPERRUNG"  #: Sperrung einer Abnahmestelle
    ENTSPERRUNG = "ENTSPERRUNG"  #: Entsperrung einer Abnahmestelle
    MAHNKOSTEN = "MAHNKOSTEN"  #: Mahnkosten
    INKASSOKOSTEN = "INKASSOKOSTEN"  #: Inkassokosten
