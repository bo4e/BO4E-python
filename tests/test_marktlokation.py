import json
from typing import Tuple

import pytest  # type:ignore[import]

from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.bo.marktlokation import Marktlokation, MarktlokationSchema
from bo4e.com.adresse import Adresse
from bo4e.enum.anrede import Anrede
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.botyp import BoTyp
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.kontaktart import Kontaktart
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.sparte import Sparte


class TestMaLo:
    def test_serialisation_only_required_attributes(self):
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
        assert malo.bo_typ is BoTyp.MARKTLOKATION, "boTyp was not automatically set"

        schema = MarktlokationSchema()

        json_string = schema.dumps(malo, ensure_ascii=False)
        json_dict = json.loads(json_string)

        assert "boTyp" in json_dict, "No camel case serialization"
        assert "marktlokationsId" in json_dict, "No camel case serialization"

        deserialized_malo: Marktlokation = schema.loads(json_string)

        # check that `deserialized_malo.marktlokations_id` and `malo.marktlokations_id` have the same value
        # but are **not** the same object.
        assert deserialized_malo.marktlokations_id == malo.marktlokations_id
        assert deserialized_malo.marktlokations_id is not malo.marktlokations_id
        assert deserialized_malo.bo_typ is BoTyp.MARKTLOKATION

    def test_serialization_required_and_optional_attributes(self):
        """
        Test serialisation of Marktlokation with required attributes and optional attributes
        """
        gp = Geschaeftspartner(
            anrede=Anrede.FRAU,
            name1="von Sinnen",
            name2="Helga",
            name3=None,
            gewerbekennzeichnung=True,
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
            unterbrechbar=True,  # optional attribute
            netzebene=Netzebene.NSP,
            endkunde=gp,
        )
        assert malo.versionstruktur == "2", "versionstruktur was not automatically set"
        assert malo.bo_typ == BoTyp.MARKTLOKATION, "boTyp was not automatically set"

        schema = MarktlokationSchema()

        json_string = schema.dumps(malo, ensure_ascii=False)
        json_dict = json.loads(json_string)

        assert "boTyp" in json_dict, "No camel case serialization"
        assert "marktlokationsId" in json_dict, "No camel case serialization"

        deserialized_malo: Marktlokation = schema.loads(json_string)

        assert deserialized_malo.marktlokations_id == malo.marktlokations_id
        assert deserialized_malo.marktlokations_id is not malo.marktlokations_id
        assert deserialized_malo.bo_typ is BoTyp.MARKTLOKATION
        assert deserialized_malo.endkunde == gp

    def test_missing_required_fields(self):
        """
        Test that the required attributes are checked in the deserialization.
        Therefore the required attribute `marktlokations_id` is removed in the test data.
        """
        invalid_json_string = """{
            "katasterinformation": null,
            "boTyp": "MARKTLOKATION",
            "endkunde": null,
            "sparte": "GAS",
            "zugehoerigeMesslokation": null,
            "verbrauchsart": null,
            "externeReferenzen": null,
            "gebietstyp": null,
            "grundversorgercodenr": null,
            "netzebene": "NSP",
            "netzbetreibercodenr": null,
            "netzgebietsnr": null,
            "lokationsadresse": {
                "ort": "Leipzig",
                "strasse": "Jahnalle",
                "adresszusatz": null,
                "coErgaenzung": null,
                "landescode": "DE",
                "postfach": null,
                "hausnummer": "1",
                "postleitzahl": "04177"
                },
            "unterbrechbar": null,
            "gasqualitaet": null,
            "bilanzierungsgebiet": null,
            "geoadresse": null,
            "bilanzierungsmethode": "PAUSCHAL",
            "versionstruktur": "2",
            "energierichtung": "EINSP"
            }"""

        schema = MarktlokationSchema()

        with pytest.raises(TypeError) as excinfo:
            schema.loads(invalid_json_string)

        assert "marktlokations_id" in str(excinfo.value)

    def test_address_validation(self):
        with pytest.raises(ValueError) as excinfo:
            _ = Marktlokation(
                marktlokations_id="51238696781",
                sparte=Sparte.GAS,
                lokationsadresse=Adresse(
                    postleitzahl="04177",
                    ort="Leipzig",
                    hausnummer="1",
                    strasse="Jahnalle",
                ),
                energierichtung=Energierichtung.EINSP,
                bilanzierungsmethode=Bilanzierungsmethode.PAUSCHAL,
                unterbrechbar=True,  # optional attribute
                netzebene=Netzebene.NSP,
                geoadresse="test",
                katasterinformation="test",
            )

        assert "No or more than one address information is given." == str(excinfo.value)

    @pytest.mark.parametrize(
        "malo_id_valid",
        [
            ("51238696781", True),
            ("41373559241", True),
            ("56789012345", True),
            ("52935155442", True),
            ("12345678910", False),
            ("asdasd", False),
            ("   ", False),
            ("  asdasdasd ", False),
            ("keine malo id", False),
            (None, False),
            ("", False),
        ],
    )
    def test_id_validation(self, malo_id_valid: Tuple[str, bool]):
        def _instantiate_malo(malo_id: str):
            _ = Marktlokation(
                marktlokations_id=malo_id,
                sparte=Sparte.GAS,
                lokationsadresse=Adresse(
                    postleitzahl="82031",
                    ort="Grünwald",
                    hausnummer="27A",
                    strasse="Nördliche Münchner Straße",
                ),
                energierichtung=Energierichtung.EINSP,
                bilanzierungsmethode=Bilanzierungsmethode.PAUSCHAL,
                unterbrechbar=True,
                netzebene=Netzebene.NSP,
            )

        if not malo_id_valid[1]:
            with pytest.raises(ValueError):
                _instantiate_malo(malo_id_valid[0])
        else:
            _instantiate_malo(malo_id_valid[0])
