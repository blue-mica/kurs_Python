import pickle

moto_base = [{"make": "BMW", "model": "F650", "capacity": "650"}, {"make": "HONDA", "model": "CBR", "capacity": "1000"},
             {"make": "SUZUKI", "model": "GS", "capacity": "500"}, {"make": "HONDA", "model": "XL", "capacity": "650"}]

with open("moto_base.pickle", "wb") as file:
    pickle.dump(moto_base, file)
