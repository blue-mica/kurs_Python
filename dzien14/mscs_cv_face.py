class Face(object):
    """
    Face contains data of one face received from json response.
    """

    def __init__(self, data: dict):
        """
        Creates Face instance.
        :param data: json with response from MSCS CV API
        """
        self.data = data
        self.rectangle = self.get_rectangle()
        self.gender = self.data['gender']
        self.age = self.data['age']
        self.description = f"Gender: {self.gender}, age: {self.age}"

    def get_rectangle(self) -> list:
        """
        Returns list with top left, and bottom right coordinates.
        :return: List with coordinates [x0, y0, x1, y1]
        """
        rect = self.data['faceRectangle']

        return [rect['left'],
                rect['top'],
                rect['left'] + rect['width'],
                rect['top'] + rect['height']
                ]


