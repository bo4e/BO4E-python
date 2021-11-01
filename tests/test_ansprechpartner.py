from bo4e.bo.ansprechpartner import Ansprechpartner, AnsprechpartnerSchema
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.com.adresse import Adresse
from bo4e.com.rufnummer import Rufnummer
from bo4e.com.zustaendigkeit import Zustaendigkeit
from bo4e.enum.anrede import Anrede
from bo4e.enum.botyp import BoTyp
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.kontaktart import Kontaktart
from bo4e.enum.rufnummernart import Rufnummernart
from bo4e.enum.themengebiet import Themengebiet
from bo4e.enum.titel import Titel


class TestAnsprechpartner:
    def test_de_serialisation_minimal_attributes(self):
        """
        Test de-/serialisation of Ansprechpartner only with required attributes
        """
        ansprechpartner = Ansprechpartner(
            # required attributes
            nachname="Müller-Schmidt",
            geschaeftspartner=Geschaeftspartner(
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
                    postleitzahl="12345",
                    ort="Sankt Musterweiler",
                    strasse="Mühlenweg",
                    hausnummer="540a",
                ),
            ),
        )
        assert ansprechpartner.versionstruktur == "2", "versionstruktur was not automatically set"
        assert ansprechpartner.bo_typ is BoTyp.ANSPRECHPARTNER, "boTyp was not automatically set"

        schema = AnsprechpartnerSchema()
        json_string = schema.dumps(ansprechpartner, ensure_ascii=False)
        assert "Müller-Schmidt" in json_string
        assert "Mühlenweg" in json_string
        assert '"FRAU"' in json_string

        deserialized_ansprechpartner = schema.loads(json_data=json_string)

        assert isinstance(deserialized_ansprechpartner, Ansprechpartner)
        assert isinstance(deserialized_ansprechpartner.geschaeftspartner, Geschaeftspartner)
        assert deserialized_ansprechpartner == ansprechpartner

    def test_de_serialisation_maximal_attributes(self):
        """
        Test de-/serialisation of Ansprechpartner only with required attributes
        """
        ansprechpartner = Ansprechpartner(
            # required attributes
            nachname="Müller-Schmidt",
            geschaeftspartner=Geschaeftspartner(
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
                    postleitzahl="12345",
                    ort="Sankt Musterweiler",
                    strasse="Mühlenweg",
                    hausnummer="540a",
                ),
            ),
            # optional attributes
            anrede=Anrede.EHELEUTE,
            individuelle_anrede="Künstler",
            titel=Titel.PROF_DR,
            vorname="Hans",
            e_mail_adresse="hans.müller@getrei.de",
            kommentar="does this thing work?",
            adresse=Adresse(
                postleitzahl="12345",
                ort="Sankt Musterweiler",
                strasse="Mühlenweg",
                hausnummer="540a",
            ),
            rufnummer=Rufnummer(nummerntyp=Rufnummernart.RUF_DURCHWAHL, rufnummer="112358132134"),
            zustaendigkeit=Zustaendigkeit(
                themengebiet=Themengebiet.MARKTKOMMUNIKATION, jobtitel="Schatzmeister", abteilung="unten rechts"
            ),
        )
        assert ansprechpartner.versionstruktur == "2", "versionstruktur was not automatically set"
        assert ansprechpartner.bo_typ is BoTyp.ANSPRECHPARTNER, "boTyp was not automatically set"

        schema = AnsprechpartnerSchema()
        json_string = schema.dumps(ansprechpartner, ensure_ascii=False)
        assert "Müller-Schmidt" in json_string
        assert "Mühlenweg" in json_string
        assert "PROF_DR" in json_string

        deserialized_ansprechpartner = schema.loads(json_data=json_string)

        assert isinstance(deserialized_ansprechpartner, Ansprechpartner)
        assert isinstance(deserialized_ansprechpartner.geschaeftspartner, Geschaeftspartner)
        assert isinstance(deserialized_ansprechpartner.adresse, Adresse)
        assert isinstance(deserialized_ansprechpartner.rufnummer, Rufnummer)
        assert isinstance(deserialized_ansprechpartner.zustaendigkeit, Zustaendigkeit)
        assert deserialized_ansprechpartner == ansprechpartner
