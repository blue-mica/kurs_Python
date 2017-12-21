from dzien14.mscs_cv import SmartPicture
from dzien14.pic_describer import PictureDescriptor

# pic_ocr = "http://twoje-seriale.pl/wp-content/uploads/2011/01/ludzie-chudego.jpg"

pic_path = "IMG_20160526_185540.jpg"
# pic_url = 'http://twoje-seriale.pl/wp-content/uploads/2011/01/ludzie-chudego.jpg'

# test tworzenia instancji i wysłania requestu
sp1 = SmartPicture(path=pic_path)
sp1.analyze()
# sp2 = SmartPicture(url=pic_url)
# sp2.analyze()

# wypiszemy info
print("Caption:", sp1.description)
print("Num of faces:", len(sp1.faces))

for face in sp1.faces:
    print(face.gender, face.age)
    print(face.rectangle)
#
# test opisywania zdjęcia
pd1 = PictureDescriptor(sp1)
pd1.describe()
#
# pd2 = PictureDescriptor(sp2)
# pd2.describe()
#
# test ocr
# sp3 = SmartPicture(url=pic_ocr)
# sp3.analyze(ocr=True)
# print(sp3.text.text)
