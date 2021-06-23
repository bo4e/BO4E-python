import json
from typing import Tuple

import pytest
from bo4e.bo.messlokation import Messlokation, MesslokationSchema
from bo4e.com.adresse import Adresse
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.botyp import BoTyp
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.netzebene import Netzebene
from bo4e.enum.sparte import Sparte


class TestMeLo:
    def test_serialisation_only_required_attributes(self):
        """
        Test serialisation of Messlokation only with required attributes
        """
        melo = Messlokation(
            messlokations_id="DE00056266802AO6G56M11SN51G21M24S",
            sparte=Sparte.STROM,
            netzebene=Netzebene.MSP,
            energierichtung=Energierichtung.EINSP,
            bilanzierungsmethode=Bilanzierungsmethode.PAUSCHAL,
        )
        assert melo.versionstruktur == "2", "versionstruktur was not automatically set"
        assert melo.bo_typ is BoTyp.MESSLOKATION, "boTyp was not automatically set"

        schema = MesslokationSchema()

        json_string = schema.dumps(melo, ensure_ascii=False)
        json_dict = json.loads(json_string)

        assert "boTyp" in json_dict, "No camel case serialization"
        assert "messlokationsId" in json_dict, "No camel case serialization"

        deserialized_melo: Messlokation = schema.loads(json_string)

        # check that `deserialized_malo.marktlokations_id` and `malo.marktlokations_id` have the same value
        # but are **not** the same object.
        assert deserialized_melo.messlokations_id == melo.messlokations_id
        assert deserialized_melo.messlokations_id is not melo.messlokations_id
        assert deserialized_melo.bo_typ is BoTyp.MESSLOKATION

    def test_serialization_required_and_optional_attributes(self):
        """
        Test serialisation of Messlokation with required attributes and optional attributes
        """

        melo = Messlokation(
            # required attributes
            messlokations_id="DE00056266802AO6G56M11SN51G21M24S",
            sparte=Sparte.STROM,
            netzebene=Netzebene.MSP,
            energierichtung=Energierichtung.EINSP,
            bilanzierungsmethode=Bilanzierungsmethode.PAUSCHAL,
            # optional attributes
            messgebietnr="664073",
            grundzustaendiger_mdl_codenr="9904768000008",
            messadresse=Adresse(postleitzahl="04177", ort="Leipzig", hausnummer="1", strasse="Jahnalle"),
        )
        assert melo.versionstruktur == "2", "versionstruktur was not automatically set"
        assert melo.bo_typ == BoTyp.MESSLOKATION, "boTyp was not automatically set"

        schema = MesslokationSchema()

        json_string = schema.dumps(melo, ensure_ascii=False)
        json_dict = json.loads(json_string)

        assert "boTyp" in json_dict, "No camel case serialization"
        assert "messlokationsId" in json_dict, "No camel case serialization"

        deserialized_melo: Messlokation = schema.loads(json_string)

        assert deserialized_melo.messlokations_id == melo.messlokations_id
        assert deserialized_melo.messlokations_id is not melo.messlokations_id
        assert deserialized_melo.bo_typ is BoTyp.MESSLOKATION

    def test_missing_required_fields(self):
        """
        Test that the required attributes are checked in the deserialization.
        Therefore the required attribute `messlokations_id` is removed in the test data.
        """
        invalid_json_string = """
            {
                "boTyp": "MESSLOKATION",
                "messlokationszaehler": null,
                "katasterinformation": null,
                "messgebietnr": "664073",
                "bilanzierungsmethode": "PAUSCHAL",
                "messadresse":
                    {
                        "strasse": "Jahnalle",
                        "hausnummer": "1",
                        "postfach": null,
                        "postleitzahl": "04177",
                        "landescode": "DE",
                        "coErgaenzung": null,
                        "adresszusatz": null,
                        "ort": "Leipzig"
                    },
                "sparte": "STROM",
                "netzebene": "MSP",
                "grundzustaendigerMsbCodenr": null,
                "geraete": null,
                "externeReferenzen": [],
                "messdienstleistung": null,
                "geoadresse": null,
                "grundzustaendigerMdlCodenr": "9904768000008",
                "versionstruktur": "2",
                "energierichtung": "EINSP",
                "grundzustaendigerMsbimCodenr": null
                }
                """

        schema = MesslokationSchema()

        with pytest.raises(TypeError) as excinfo:
            schema.loads(invalid_json_string)

        assert "messlokations_id" in str(excinfo.value)

    def test_address_validation(self):
        with pytest.raises(ValueError) as excinfo:
            _ = Messlokation(
                messlokations_id="DE00056266802AO6G56M11SN51G21M24S",
                sparte=Sparte.STROM,
                netzebene=Netzebene.MSP,
                energierichtung=Energierichtung.EINSP,
                bilanzierungsmethode=Bilanzierungsmethode.PAUSCHAL,
                messadresse=Adresse(postleitzahl="04177", ort="Leipzig", hausnummer="1", strasse="Jahnalle"),
                geoadresse="test",
                katasterinformation="test",
            )

        assert "More than one address information is given." == str(excinfo.value)

    @pytest.mark.parametrize(
        "melo_id_valid",
        [
            ("DE00056266802AO6G56M11SN51G21M24S", True),
            ("FR00056266802AO6G56M11SN51G21M24S", True),
            ("0000056266802AO6G56M11SN51G21M24S", False),
            ("asdasd", False),
            ("   ", False),
            ("  asdasdasd ", False),
            ("keine melo id", False),
            (None, False),
            ("", False),
        ],
    )
    def test_id_validation(self, melo_id_valid: Tuple[str, bool]):
        def _instantiate_melo(melo_id: str):
            _ = Messlokation(
                messlokations_id=melo_id,
                sparte=Sparte.STROM,
                netzebene=Netzebene.MSP,
                energierichtung=Energierichtung.EINSP,
                bilanzierungsmethode=Bilanzierungsmethode.PAUSCHAL,
            )

        if not melo_id_valid[1]:
            with pytest.raises(ValueError):
                _instantiate_melo(melo_id_valid[0])
        else:
            _instantiate_melo(melo_id_valid[0])
