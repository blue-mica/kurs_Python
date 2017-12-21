import json
import os
import requests
import shutil
from dzien14.configuration import *
from dzien14.mscs_cv_face import Face
from dzien14.mscs_cv_text import Text
from tools.pobieracz import pobierz


class SmartPicture(object):
    """
    This is a smart picture - it holds information about picture that is being processed by
    Microsoft Cognitive Services Computer Vision API
    """

    PICS_COUNT = 0

    def __init__(self, path=None, url=None):
        """
        Creates SmartPicture. Path will be taken before url.
        If both values are given, then path will be taken to request.

        :param path: Path to picture on computer.
        :param url: URL to picture on the Internet.
        """
        SmartPicture.PICS_COUNT += 1

        self.path = path
        self.url = url

        self.extension = None
        self.height = None
        self.id = SmartPicture.PICS_COUNT
        self.pic_info = None
        self.pic_source_path = None
        self.pic_target_path = None
        self.request_body = None
        self.request_header = None
        self.text = None

        self.__faces = None

        self.__prepare_request()

    def __prepare_request(self):
        """
        Prepares request's header and body (if picture is locally on computer).
        :return: None
        """

        self.__prepare_target_path()

        if self.path is not None and os.path.exists(self.path):
            self.request_header = HEADER_PIC

        elif self.url is not None:
            self.request_header = HEADER_URL
            self.request_body = {'url': f'{self.url}'}

        else:
            print("No proper path or url provided!")
            return

    def __prepare_target_path(self):
        """
        Creates comman part of target path - {target dir}\{root name}_{id}_
        Target path is being used to save json, source and described picture.
        """
        target_dir = os.path.join(os.getcwd(), TARGET_DIR)

        if not os.path.exists(target_dir):
            os.mkdir(target_dir)

        self.pic_target_path = os.path.join(target_dir, ROOT_NAME)
        self.pic_target_path += str(self.id)

    def analyze(self, ocr=False):
        """
        Sends request and seeds fields with received data.
        :param: ocr: If True, then OCR endpoint will be called, else anylyze endpoint.
        :return: None
        """
        print("Sending request...")

        api_url = OCR_URL if ocr else API_URL

        if self.path is not None:
            response = self.send_picture(api_url)
            self.__save_source_picture()

        elif self.url is not None:
            response = self.send_picture_url(api_url)
            self.__save_source_picture()

        else:
            print("No proper path or url given, cannot send request")
            return

        self.pic_info = json.loads(response.text, encoding="utf-8")

        try:
            self.height = self.pic_info['metadata']['height']
        except KeyError:
            pass

        self.__save_json_info()

        if ocr:
            self.get_ocr_txt()

    def get_ocr_txt(self):
        self.text = Text(self.pic_info)
        target_txt = self.pic_target_path + '.txt'
        with open(target_txt, 'w') as file:
            file.write(self.text.text)

    def send_picture(self, api_url) -> requests.Response:
        """
        Sends picture to process. Raises response for status.
        :param: api_url: API endpoint.
        :return: Response.
        """
        pic_bytes = open(self.path, 'rb').read()
        response = requests.post(api_url,
                                 data=pic_bytes,
                                 headers=self.request_header,
                                 params=PARAMS)
        response.raise_for_status()
        return response

    def send_picture_url(self, api_url) -> requests.Response:
        """
        Sends request with picture url. Raises response for status.
        :param: api_url: API endpoint.
        :return: Response.
        """
        response = requests.post(api_url,
                                 json=self.request_body,
                                 headers=self.request_header,
                                 params=PARAMS)
        response.raise_for_status()
        return response

    def __save_json_info(self):
        """
        Saves json with received data.
        """
        full_name = self.pic_target_path + ".json"

        with open(full_name, 'w') as file:
            json.dump(self.pic_info, file, indent=4, ensure_ascii=False)
            print(f"Saved JSON at location: {full_name}")

    def __save_source_picture(self):
        """
        Saves source picture with changed name to root_{id}_source in target directory.
        """

        pic_path = "{root}_source{ext}"

        if self.path is not None:
            self.extension = os.path.splitext(self.path)[1]
            self.pic_source_path = pic_path.format(root=self.pic_target_path, ext=self.extension)
            shutil.copy(self.path, self.pic_source_path)

        elif self.url is not None:
            pic_name = os.path.basename(self.url)
            self.extension = os.path.splitext(pic_name)[1]

            if self.extension == "":
                self.extension = ".jpg"

            self.pic_source_path = pic_path.format(root=self.pic_target_path, ext=self.extension)

            pobierz(self.url, self.pic_source_path)

        else:
            print("Did not saved picture, incorrect path or url!")
            return

        print(f"Saved source picture in: {self.pic_source_path}")

    # def get_ocr(self):


    @property
    def description(self) -> str:
        """
        Gets recognized description.
        """
        captions = self.pic_info['description']['captions']

        if len(captions) > 0:
            return captions[0]['text']
        else:
            return "No description"

    @property
    def faces(self) -> list:
        """
        Gets list containing Face objects.
        :return: List of faces [Face, ...]
        """

        if self.__faces is None:
            self.__faces = []
            for face_data in self.pic_info['faces']:
                face = Face(face_data)
                self.__faces.append(face)

        return self.__faces

    @property
    def celebrities(self):
        """
        Gets infor about recognized celebrities.
        """
        # todo Implement it
        return None
