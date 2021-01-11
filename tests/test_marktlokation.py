import json
import pytest

from typing import Tuple

from bo4e.bo.marktlokation import Marktlokation, MarktlokationSchema
from bo4e.com.adresse import Adresse
from bo4e.enum.bilanzierungsmethode import Bilanzierungsmethode
from bo4e.enum.botyp import BoTyp
from bo4e.enum.energierichtung import Energierichtung
from bo4e.enum.sparte import Sparte
from bo4e.enum.netzebene import Netzebene


class TestMaLo:
    def test_serialization(self):
        malo = Marktlokation(
            marktlokations_id="51238696781",
            sparte=Sparte.GAS,
            lokationsadresse=Adresse(
                postleitzahl="04177", ort="Leipzig", hausnummer="1", strasse="Jahnalle"
            ),
            energierichtung=Energierichtung.EINSP,
            bilanzierungsmethode=Bilanzierungsmethode.PAUSCHAL,
            unterbrechbar=True,  # optional attribute
            netzebene=Netzebene.NSP,
        )
        assert malo.versionstruktur == 2, "versionstruktur was not automatically set"
        assert malo.bo_typ == BoTyp.MARKTLOKATION, "boTyp was not automatically set"

        schema = MarktlokationSchema()

        json_string = schema.dumps(malo, ensure_ascii=False)
        json_dict = json.loads(json_string)

        assert "boTyp" in json_dict, "No camel case serialization"
        assert "marktlokationsId" in json_dict, "No camel case serialization"

        deserialized_malo: Marktlokation = schema.loads(json_string)

        assert deserialized_malo.marktlokations_id == malo.marktlokations_id
        assert deserialized_malo.marktlokations_id is not malo.marktlokations_id

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
