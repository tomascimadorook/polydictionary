class PolyDictionary:

    def __init__(self):
        self._dictionary = {
            "car": "a motor vehicle with four wheels; "
            "usually propelled by an internal combustion engine",
            "bike": "a motor vehicle with two wheels and a strong frame",
        }
        self._synonyms = {"car": "automobile", "bike": "motorcycle"}

    def define(self, word: str) -> str:
        return self._dictionary.get(word)

    def synonym(self, word: str) -> str:
        return self._synonyms.get(word)
