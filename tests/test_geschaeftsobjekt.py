import pytest
from pydantic import ValidationError

from bo4e import Geschaeftsobjekt, Typ
from bo4e.zusatzattribut import ZusatzAttribut
from tests.serialization_helper import assert_serialization_roundtrip


class TestGeschaeftsobjekt:
    @pytest.mark.parametrize(
        "geschaeftsobjekt",
        [
            Geschaeftsobjekt(
                typ=Typ.ENERGIEMENGE,
                version="2",
                zusatz_attribute=[
                    ZusatzAttribut(name="HOCHFREQUENZ_HFSAP_100", wert="12345"),
                    ZusatzAttribut(name="Schufa-ID", wert="aksdlakoeuhn"),
                ],
            ),
            Geschaeftsobjekt(
                typ=Typ.ENERGIEMENGE,
                version="2",
                zusatz_attribute=[],
            ),
        ],
    )
    def test_serialization_roundtrip(self, geschaeftsobjekt: Geschaeftsobjekt) -> None:
        """
        Test de-/serialisation of Geschaeftsobjekt
        """
        assert_serialization_roundtrip(geschaeftsobjekt)

    def test_no_list_in_externen_referenzen(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Geschaeftsobjekt(
                typ=Typ.ENERGIEMENGE,
                zusatz_attribute=ZusatzAttribut(name="Schufa-ID", wert="aksdlakoeuhn"),  # type: ignore[arg-type]
            )
        # The error message is completely broken, but who cares
        assert "2 validation error" in str(excinfo.value)
        assert "type=model_type" in str(excinfo.value)
