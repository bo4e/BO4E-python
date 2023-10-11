from bo4e import (
    Adresse,
    Anrede,
    Ansprechpartner,
    Geschaeftspartner,
    Geschaeftspartnerrolle,
    Kontaktart,
    Rufnummer,
    Rufnummernart,
    Themengebiet,
    Titel,
    Typ,
    Zustaendigkeit,
)


class TestAnsprechpartner:
    def test_de_serialisation_minimal_attributes(self) -> None:
        """
        Test de-/serialisation of Ansprechpartner only with required attributes
        """
        ansprechpartner = Ansprechpartner(
            nachname="Müller-Schmidt",
            geschaeftspartner=Geschaeftspartner(
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
                    postleitzahl="12345",
                    ort="Sankt Musterweiler",
                    strasse="Mühlenweg",
                    hausnummer="540a",
                ),
            ),
        )
        assert ansprechpartner.version is not None, "versionstruktur was not automatically set"
        assert ansprechpartner.typ is Typ.ANSPRECHPARTNER, "_typ was not automatically set"

        json_string = ansprechpartner.model_dump_json(by_alias=True)
        assert "Müller-Schmidt" in json_string
        assert "Mühlenweg" in json_string
        assert '"FRAU"' in json_string

        deserialized_ansprechpartner = Ansprechpartner.model_validate_json(json_string)

        assert isinstance(deserialized_ansprechpartner, Ansprechpartner)
        assert isinstance(deserialized_ansprechpartner.geschaeftspartner, Geschaeftspartner)
        assert deserialized_ansprechpartner == ansprechpartner

    def test_de_serialisation_maximal_attributes(self) -> None:
        """
        Test de-/serialisation of Ansprechpartner only with required attributes
        """
        ansprechpartner = Ansprechpartner(
            nachname="Müller-Schmidt",
            geschaeftspartner=Geschaeftspartner(
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
                    postleitzahl="12345",
                    ort="Sankt Musterweiler",
                    strasse="Mühlenweg",
                    hausnummer="540a",
                ),
            ),
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
        assert ansprechpartner.version is not None, "versionstruktur was not automatically set"
        assert ansprechpartner.typ is Typ.ANSPRECHPARTNER, "_typ was not automatically set"

        json_string = ansprechpartner.model_dump_json(by_alias=True)
        assert "Müller-Schmidt" in json_string
        assert "Mühlenweg" in json_string
        assert "PROF_DR" in json_string

        deserialized_ansprechpartner = Ansprechpartner.model_validate_json(json_string)

        assert isinstance(deserialized_ansprechpartner, Ansprechpartner)
        assert isinstance(deserialized_ansprechpartner.geschaeftspartner, Geschaeftspartner)
        assert isinstance(deserialized_ansprechpartner.adresse, Adresse)
        assert isinstance(deserialized_ansprechpartner.rufnummer, Rufnummer)
        assert isinstance(deserialized_ansprechpartner.zustaendigkeit, Zustaendigkeit)
        assert deserialized_ansprechpartner == ansprechpartner
