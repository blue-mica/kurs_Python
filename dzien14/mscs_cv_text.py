class Text(object):
    """
    Represents text from smart image
    """
    def __init__(self, data: dict):
        self.data = data
        self.language = data['language']
        self.text = self.__extract_text()

    def __extract_text(self):
        """
        Extracts text from json.
        :return: String containing all text.
        """
        text = ''

        #todo wziąc tekst ze słow z każdej linijki z każdego regionu

        return text




