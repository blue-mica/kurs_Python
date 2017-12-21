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

        for region in self.data['regions']:

            for line in region['lines']:

                line_text = ''

                for word in line['words']:
                    line_text += f"{word['text']} "

                text += f"{line_text}".strip()
                text += "\n"

        return text





