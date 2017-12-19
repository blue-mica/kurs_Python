from dzien14.mscs_cv import SmartPicture
from dzien14.pic_describer import PictureDescriptor

pic_ocr = "http://imgc.allpostersimages.com/img/posters/watch-your-thoughts-motivational-poster_u-L-F5BH0S0.jpg"

pic_path = "friends.jpg"
pic_url = 'https://qph.ec.quoracdn.net/main-qimg-71e8b8cddfce751d8e0a8ed45b316731-c'

# test tworzenia instancji i wysłania requestu
sp1 = SmartPicture(path=pic_path)
sp1.analyze()
sp2 = SmartPicture(url=pic_url)
sp2.analyze()

# wypiszemy info
# print("Caption:", sp1.description)
# print("Num of faces:", len(sp1.faces))
#
# for face in sp1.faces:
#     print(face.gender, face.age)
#     print(face.rectangle)
#
# # test opisywania zdjęcia
# pd1 = PictureDescriptor(sp1)
# pd1.describe()
#
# pd2 = PictureDescriptor(sp2)
# pd2.describe()
#
# # test ocr
# sp3 = SmartPicture(url=pic_ocr)
# sp3.analyze(ocr=True)
# print(sp3.text.text)
