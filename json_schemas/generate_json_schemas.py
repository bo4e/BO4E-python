"""
This script is run in the tox 'json_schemas' environment.
It creates json schema files as described in the README.md in the same directory.
"""

import json
import pathlib
from typing import List, Type

from marshmallow import Schema, fields
from marshmallow_jsonschema import JSONSchema  # type:ignore[import]

from bo4e.bo.angebot import AngebotSchema
from bo4e.bo.ansprechpartner import AnsprechpartnerSchema
from bo4e.bo.ausschreibung import AusschreibungSchema
from bo4e.bo.buendelvertrag import BuendelvertragSchema
from bo4e.bo.energiemenge import EnergiemengeSchema
from bo4e.bo.fremdkosten import FremdkostenSchema
from bo4e.bo.geschaeftspartner import GeschaeftspartnerSchema
from bo4e.bo.kosten import KostenSchema
from bo4e.bo.lastgang import LastgangKompaktSchema, LastgangSchema
from bo4e.bo.marktlokation import MarktlokationSchema
from bo4e.bo.marktteilnehmer import MarktteilnehmerSchema
from bo4e.bo.messlokation import MesslokationSchema
from bo4e.bo.netznutzungsrechnung import NetznutzungsrechnungSchema
from bo4e.bo.preisblatt import PreisblattSchema
from bo4e.bo.preisblattdienstleistung import PreisblattDienstleistungSchema
from bo4e.bo.preisblatthardware import PreisblattHardwareSchema
from bo4e.bo.preisblattkonzessionsabgabe import PreisblattKonzessionsabgabeSchema
from bo4e.bo.preisblattmessung import PreisblattMessungSchema
from bo4e.bo.preisblattnetznutzung import PreisblattNetznutzungSchema
from bo4e.bo.rechnung import RechnungSchema
from bo4e.bo.region import RegionSchema
from bo4e.bo.regionaltarif import RegionaltarifSchema
from bo4e.bo.standorteigenschaften import StandorteigenschaftenSchema
from bo4e.bo.tarif import TarifSchema
from bo4e.bo.tarifinfo import TarifinfoSchema
from bo4e.bo.tarifkosten import TarifkostenSchema
from bo4e.bo.tarifpreisblatt import TarifpreisblattSchema
from bo4e.bo.vertrag import VertragSchema
from bo4e.bo.zaehler import ZaehlerSchema
from bo4e.bo.zeitreihe import ZeitreiheSchema
from bo4e.com.adresse import AdresseSchema
from bo4e.com.angebotsposition import AngebotspositionSchema
from bo4e.com.angebotsteil import AngebotsteilSchema
from bo4e.com.angebotsvariante import AngebotsvarianteSchema
from bo4e.com.aufabschlag import AufAbschlagSchema
from bo4e.com.aufabschlagproort import AufAbschlagProOrtSchema
from bo4e.com.aufabschlagregional import AufAbschlagRegionalSchema
from bo4e.com.aufabschlagstaffelproort import AufAbschlagstaffelProOrtSchema
from bo4e.com.ausschreibungsdetail import AusschreibungsdetailSchema
from bo4e.com.ausschreibungslos import AusschreibungslosSchema
from bo4e.com.betrag import BetragSchema
from bo4e.com.dienstleistung import DienstleistungSchema
from bo4e.com.energieherkunft import EnergieherkunftSchema
from bo4e.com.energiemix import EnergiemixSchema
from bo4e.com.externereferenz import ExterneReferenzSchema
from bo4e.com.fremdkostenblock import FremdkostenblockSchema
from bo4e.com.fremdkostenposition import FremdkostenpositionSchema
from bo4e.com.geokoordinaten import GeokoordinatenSchema
from bo4e.com.geraet import GeraetSchema
from bo4e.com.geraeteeigenschaften import GeraeteeigenschaftenSchema
from bo4e.com.hardware import HardwareSchema
from bo4e.com.katasteradresse import KatasteradresseSchema
from bo4e.com.kostenblock import KostenblockSchema
from bo4e.com.kostenposition import KostenpositionSchema
from bo4e.com.kriteriumwert import KriteriumWertSchema
from bo4e.com.marktgebietinfo import MarktgebietInfoSchema
from bo4e.com.menge import MengeSchema
from bo4e.com.messlokationszuordnung import MesslokationszuordnungSchema
from bo4e.com.positionsaufabschlag import PositionsAufAbschlagSchema
from bo4e.com.preis import PreisSchema
from bo4e.com.preisgarantie import PreisgarantieSchema
from bo4e.com.preisposition import PreispositionSchema
from bo4e.com.preisstaffel import PreisstaffelSchema
from bo4e.com.rechnungsposition import RechnungspositionSchema
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeitSchema
from bo4e.com.regionalepreisgarantie import RegionalePreisgarantieSchema
from bo4e.com.regionalepreisstaffel import RegionalePreisstaffelSchema
from bo4e.com.regionaleraufabschlag import RegionalerAufAbschlagSchema
from bo4e.com.regionaletarifpreisposition import RegionaleTarifpreispositionSchema
from bo4e.com.regionskriterium import RegionskriteriumSchema
from bo4e.com.rufnummer import RufnummerSchema
from bo4e.com.sigmoidparameter import SigmoidparameterSchema
from bo4e.com.standorteigenschaftenallgemein import StandorteigenschaftenAllgemeinSchema
from bo4e.com.standorteigenschaftengas import StandorteigenschaftenGasSchema
from bo4e.com.standorteigenschaftenstrom import StandorteigenschaftenStromSchema
from bo4e.com.steuerbetrag import SteuerbetragSchema
from bo4e.com.tagesvektor import TagesvektorSchema
from bo4e.com.tarifberechnungsparameter import TarifberechnungsparameterSchema
from bo4e.com.tarifeinschraenkung import TarifeinschraenkungSchema
from bo4e.com.tarifpreis import TarifpreisSchema
from bo4e.com.tarifpreisposition import TarifpreispositionSchema
from bo4e.com.tarifpreispositionproort import TarifpreispositionProOrtSchema
from bo4e.com.tarifpreisstaffelproort import TarifpreisstaffelProOrtSchema
from bo4e.com.unterschrift import UnterschriftSchema
from bo4e.com.verbrauch import VerbrauchSchema
from bo4e.com.vertragskonditionen import VertragskonditionenSchema
from bo4e.com.vertragsteil import VertragsteilSchema
from bo4e.com.zaehlwerk import ZaehlwerkSchema
from bo4e.com.zeitintervall import ZeitintervallSchema
from bo4e.com.zeitraum import ZeitraumSchema
from bo4e.com.zeitreihenwert import ZeitreihenwertSchema
from bo4e.com.zeitreihenwertkompakt import ZeitreihenwertkompaktSchema
from bo4e.com.zustaendigkeit import ZustaendigkeitSchema

schema_types: List[Type[Schema]] = [
    AngebotSchema,
    AnsprechpartnerSchema,
    AusschreibungSchema,
    BuendelvertragSchema,
    EnergiemengeSchema,
    FremdkostenSchema,
    GeschaeftspartnerSchema,
    KostenSchema,
    LastgangSchema,
    LastgangKompaktSchema,
    MarktlokationSchema,
    MarktteilnehmerSchema,
    MesslokationSchema,
    NetznutzungsrechnungSchema,
    PreisblattSchema,
    PreisblattDienstleistungSchema,
    PreisblattHardwareSchema,
    PreisblattKonzessionsabgabeSchema,
    PreisblattMessungSchema,
    PreisblattNetznutzungSchema,
    RechnungSchema,
    RegionSchema,
    RegionaltarifSchema,
    StandorteigenschaftenSchema,
    TarifSchema,
    TarifinfoSchema,
    TarifkostenSchema,
    TarifpreisblattSchema,
    VertragSchema,
    ZaehlerSchema,
    ZeitreiheSchema,
    # COMs
    AdresseSchema,
    AngebotspositionSchema,
    AngebotsteilSchema,
    AngebotsvarianteSchema,
    AufAbschlagSchema,
    AufAbschlagProOrtSchema,
    AufAbschlagRegionalSchema,
    AufAbschlagstaffelProOrtSchema,
    AusschreibungsdetailSchema,
    AusschreibungslosSchema,
    BetragSchema,
    DienstleistungSchema,
    EnergieherkunftSchema,
    EnergiemixSchema,
    ExterneReferenzSchema,
    FremdkostenblockSchema,
    FremdkostenpositionSchema,
    GeokoordinatenSchema,
    GeraetSchema,
    GeraeteeigenschaftenSchema,
    HardwareSchema,
    KatasteradresseSchema,
    KostenblockSchema,
    KostenpositionSchema,
    KriteriumWertSchema,
    MarktgebietInfoSchema,
    MengeSchema,
    MesslokationszuordnungSchema,
    PositionsAufAbschlagSchema,
    PreisSchema,
    PreisgarantieSchema,
    PreispositionSchema,
    PreisstaffelSchema,
    RechnungspositionSchema,
    RegionaleGueltigkeitSchema,
    RegionalePreisgarantieSchema,
    RegionalePreisstaffelSchema,
    RegionalerAufAbschlagSchema,
    RegionaleTarifpreispositionSchema,
    RegionskriteriumSchema,
    RufnummerSchema,
    SigmoidparameterSchema,
    StandorteigenschaftenAllgemeinSchema,
    StandorteigenschaftenGasSchema,
    StandorteigenschaftenStromSchema,
    SteuerbetragSchema,
    TagesvektorSchema,
    TarifberechnungsparameterSchema,
    TarifeinschraenkungSchema,
    TarifpreisSchema,
    TarifpreispositionSchema,
    TarifpreispositionProOrtSchema,
    TarifpreisstaffelProOrtSchema,
    UnterschriftSchema,
    VerbrauchSchema,
    VertragskonditionenSchema,
    VertragsteilSchema,
    ZaehlwerkSchema,
    ZeitintervallSchema,
    ZeitraumSchema,
    ZeitreihenwertSchema,
    ZeitreihenwertkompaktSchema,
    ZustaendigkeitSchema,
]
json_schema = JSONSchema()
for schema_type in schema_types:
    this_directory = pathlib.Path(__file__).parent.absolute()
    file_name = schema_type.__name__ + ".json"  # pylint:disable=invalid-name
    if "bo4e.bo." in str(schema_type.class_name):
        file_path = this_directory / "bo" / file_name
    elif "bo4e.com." in str(schema_type.class_name):
        file_path = this_directory / "com" / file_name
    else:
        file_path = this_directory / file_name
    # atlassian_url = f"""
    # .. HINT::
    #     `{schema_type.__name__[:len(schema_type.__name__)-6]} JSON Schema <https://json-schema.app/view/%23?url=https://raw.githubusercontent.com/Hochfrequenz/BO4E-python/main/json_schemas/bo/{file_name}>`_
    # """
    # print(atlassian_url)
    schema_instance = schema_type()
    json_schema_dict = json_schema.dump(schema_instance)
    with open(file_path, "w", encoding="utf-8") as json_schema_file:
        json.dump(json_schema_dict, json_schema_file, ensure_ascii=False, sort_keys=True, indent=4)
