from decimal import Decimal
from typing import Tuple

import pytest
from pydantic import ValidationError

from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.bo.marktlokation import Marktlokation
from bo4e.com.adresse import Adresse
from bo4e.com.geokoordinaten import Geokoordinaten
from bo4e.enum.anrede import Anrede
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.kontaktart import Kontaktart
from bo4e.enum.kundentyp import Kundentyp
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.sparte import Sparte
from bo4e.enum.typ import Typ


class TestMaLo:
    def test_serialisation_only_required_attributes(self) -> None:
        """
        Test serialisation of Marktlokation only with required attributes
        """
        malo = Marktlokation(
            marktlokations_id="51238696781",
            sparte=Sparte.GAS,
            lokationsadresse=Adresse(postleitzahl="04177", ort="Leipzig", hausnummer="1", strasse="Jahnalle"),
            energierichtung=Energierichtung.EINSP,
            bilanzierungsmethode=Bilanzierungsmethode.PAUSCHAL,
            netzebene=Netzebene.NSP,
        )
        assert malo.versionstruktur == "2", "versionstruktur was not automatically set"
        assert malo.typ is Typ.MARKTLOKATION, "_typ was not automatically set"

        json_string = malo.model_dump_json(by_alias=True)

        assert "_typ" in json_string, "No camel case serialization"
        assert "marktlokationsId" in json_string, "No camel case serialization"

        deserialized_malo: Marktlokation = Marktlokation.model_validate_json(json_string)

        # check that `deserialized_malo.marktlokations_id` and `malo.marktlokations_id` have the same value
        # but are **not** the same object.
        assert deserialized_malo.marktlokations_id == malo.marktlokations_id
        assert deserialized_malo.marktlokations_id is not malo.marktlokations_id
        assert deserialized_malo.typ is Typ.MARKTLOKATION

    def test_serialization_required_and_optional_attributes(self) -> None:
        """
        Test serialisation of Marktlokation with required attributes and optional attributes
        """
        gp = Geschaeftspartner(
            anrede=Anrede.FRAU,
            name1="von Sinnen",
            name2="Helga",
            name3=None,
            ist_gewerbe=True,
            hrnummer="HRB 254466",
            amtsgericht="Amtsgericht München",
            kontaktweg=[Kontaktart.E_MAIL],
            umsatzsteuer_id="DE267311963",
            glaeubiger_id="DE98ZZZ09999999999",
            e_mail_adresse="test@bo4e.de",
            website="bo4e.de",
            geschaeftspartnerrolle=[Geschaeftspartnerrolle.DIENSTLEISTER],
            partneradresse=Adresse(
                postleitzahl="82031",
                ort="Grünwald",
                strasse="Nördliche Münchner Straße",
                hausnummer="27A",
            ),
        )
        malo = Marktlokation(
            marktlokations_id="51238696781",
            sparte=Sparte.GAS,
            lokationsadresse=Adresse(postleitzahl="04177", ort="Leipzig", hausnummer="1", strasse="Jahnalle"),
            energierichtung=Energierichtung.EINSP,
            bilanzierungsmethode=Bilanzierungsmethode.PAUSCHAL,
            ist_unterbrechbar=True,  # optional attribute
            netzebene=Netzebene.NSP,
            endkunde=gp,
            kundengruppen=[Kundentyp.GEWERBE, Kundentyp.PRIVAT],
        )
        assert malo.versionstruktur == "2", "versionstruktur was not automatically set"
        assert malo.typ == Typ.MARKTLOKATION, "_typ was not automatically set"

        json_string = malo.model_dump_json(by_alias=True)

        assert "_typ" in json_string, "No camel case serialization"
        assert "marktlokationsId" in json_string, "No camel case serialization"

        deserialized_malo: Marktlokation = Marktlokation.model_validate_json(json_string)

        assert deserialized_malo.marktlokations_id == malo.marktlokations_id
        assert deserialized_malo.marktlokations_id is not malo.marktlokations_id
        assert deserialized_malo.typ is Typ.MARKTLOKATION
        assert deserialized_malo.endkunde == gp
