# shallow copy - kopiowane sa tylko referencje do listy a nie ona sama

nabial = ["jajka", "mleko", "twarog"]
chemia = ["domestos", "plyn do naczyn", "proszek do prania"]

zakupy_listopad = [nabial, chemia]

zakupy_grudzien = zakupy_listopad.copy()
zakupy_styczen = zakupy_listopad[:]

print(f"Zakupy listopad {zakupy_listopad}")
print(f"Zakupy grudzien {zakupy_grudzien}")
print(f"Zakupy styczen {zakupy_styczen}")

zakupy_grudzien[0].append("maka")

print(f"Zakupy grudzien {zakupy_grudzien}")
print(f"Zakupy styczen {zakupy_styczen}")
print(f"Zakupy styczen {zakupy_styczen}")