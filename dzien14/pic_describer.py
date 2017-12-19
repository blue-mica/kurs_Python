from dzien14.mscs_cv_face import Face
from dzien14.mscs_cv import SmartPicture
from PIL import Image, ImageDraw, ImageFont

FONT_NAME = "arial.ttf"
FACE_DESC_FONT_RATIO = 1 / 8
CAPTION_FONT_RATIO = 1 / 25


class PictureDescriptor(object):
    """
    Picture descriptor - draws descriptions and faces in SmartPicture object.
    """

    def __init__(self, smart_pic: SmartPicture):
        """
        Creates descriptor of picture.
        :param smart_pic: SmartPicture object
        """
        self.smart_pic = smart_pic
        self.image = None
        self.drawer = None

        self.__set_drawer()

    def __del__(self):
        """
        Closes image before destructing instance.
        """
        self.image.close()

    def __set_drawer(self):
        """
        Sets drawer engine. Drawer draws texts and shapes on picture.
        """
        print("Setting drawer")
        source_img = Image.open(self.smart_pic.pic_source_path)
        assert isinstance(source_img, Image.Image)
        self.image = source_img.copy()
        self.drawer = ImageDraw.ImageDraw(self.image)

    def describe(self):
        """
        Describes picture with data from smart image.
        """
        self.__draw_face_info()
        self.__draw_description()
        self.__save()

    def __draw_face_info(self):
        """
        Draws face rectangles, gender and age.
        """
        assert isinstance(self.drawer, ImageDraw.ImageDraw)

        for face in self.smart_pic.faces:
            self.drawer.rectangle(face.rectangle)
            self.__draw_face_description(face)

    def __draw_description(self):
        """
        Draws description of picture.
        """
        position = (20, 20)
        color = (41, 178, 39)

        font_size = round(self.smart_pic.height * CAPTION_FONT_RATIO)
        font = PictureDescriptor.get_font(font_size)

        self.drawer.text(position, self.smart_pic.description, color, font)

    def __save(self):
        """
        Saves described picture.
        """
        assert isinstance(self.image, Image.Image)
        target_name = self.smart_pic.pic_target_path + self.smart_pic.extension
        print("Saving picture as:", target_name)
        self.image.save(target_name)

    def __draw_face_description(self, face: Face):
        """
        Draws face description - gender and age.
        :param face: Face object.
        """
        font_size = round((face.rectangle[3] - face.rectangle[1]) * FACE_DESC_FONT_RATIO)
        face_desc_pos = (face.rectangle[0], face.rectangle[1] - font_size * 2)

        color = (123, 104, 238)
        font = PictureDescriptor.get_font(font_size)

        assert isinstance(self.drawer, ImageDraw.ImageDraw)
        self.drawer.text(face_desc_pos, face.description, color, font)

    @staticmethod
    def get_font(size: int) -> ImageFont.ImageFont:
        """
        Tries to get user font, if fails, then uses default
        :param size: Size of font.
        :return: ImageFont object.
        """
        try:
            text_font = ImageFont.truetype(FONT_NAME, size)
        except IOError:
            print("Could not load chosen font, switching to default.")
            text_font = ImageFont.load_default()

        return text_font
