import json


class Marktlokation(json.JSONEncoder):
    """
    Objekt zur Aufnahme der Informationen zu einer Marktlokation
    """

    def __init__(self, marktlokationsId: str):
        self.marktlokationsId = marktlokationsId

    def default(self, o):
        return o.__dict__
