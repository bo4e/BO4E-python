import unittest

from bo4e.com.adresse import Adresse
from bo4e.enum.landescode import Landescode


class AdressTest(unittest.TestCase):
    def test_serialization(self):
        a = Adresse(postleitzahl="82031", ort="Grünwald", strasse="Nördliche Münchner Straße", hausnummer="27A")
        address_json = a.to_json()
        self.assertTrue("\"DE\"" in address_json, "Landescode did not default to 'DE'")
        json_string = r'{"strasse":"Getreidegasse", "hausnummer":"9", "ort":"Salzburg", "postleitzahl":"5020", ' \
                      r'"landescode":"AT"} '
        b: Adresse = Adresse.from_json(json_string)
        self.assertEqual(b.landescode, Landescode("Austria"))
