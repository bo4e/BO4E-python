import unittest

from bo4e.bo.marktlokation import Marktlokation
from bo4e.com.adresse import Adresse
from bo4e.enum.sparte import Sparte


class MaLoTest(unittest.TestCase):
    def test_serializable(self):
        malo = Marktlokation(
            marktlokations_id="54321012345",
            sparte=Sparte.GAS,
            lokationsadresse=Adresse(
                postleitzahl="04177", ort="Leipzig", hausnummer="1", strasse="Jahnalle"
            ),
        )
        self.assertEqual(
            malo.versionstruktur, 1, "versionstruktur was not automatically set"
        )
        self.assertEqual(
            malo.bo_typ, "MARKTLOKATION", "boTyp was not automatically set"
        )
        json_string = malo.to_json()
        self.assertTrue(
            "boTyp" in json_string, "No camel case serialization"
        )  # camel case serialization
        self.assertTrue(
            "marktlokationsId" in json_string, "No camel case serialization"
        )  # camel case serialization
        deserialized_malo: Marktlokation = Marktlokation.from_json(json_string)
        self.assertEqual(malo.marktlokations_id, deserialized_malo.marktlokations_id)
        self.assertFalse(malo.marktlokations_id is deserialized_malo.marktlokations_id)

    def test_malo_must_not_be_initialized_without_required_fields(self):
        """
        Business Objects need to be instantiated with all required values.
        :return:
        """
        with self.assertRaises(TypeError):
            _ = Marktlokation()


if __name__ == "__main__":
    unittest.main()
