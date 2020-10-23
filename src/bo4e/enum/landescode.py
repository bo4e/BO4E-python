import iso3166


class Landescode:
    """
    Der ISO-Landescode.
    """

    def __init__(self, value: str):
        """
        initialize c
        :param value:
        """
        self._country: iso3166.Country
        lookup = iso3166._CountryLookup()
        try:
            self._country = lookup.get(value)
        except KeyError:
            raise ValueError(f"'{value}' is not a valid ISO alpha2 country code.")

    @staticmethod
    def json_encoder(value) -> str:
        if not value:
            return "DE"  # default
        return Landescode(value)._country.alpha2

    @staticmethod
    def json_decoder(value: str):
        return Landescode(value)

    def __eq__(self, other):
        if isinstance(other, str):
            return Landescode(other)._country.alpha2 == self._country.alpha2
        return other._country.alpha2 == self._country.alpha2
