# deep copy - kopiowane calej listy

import copy

nabial = ["jajka", "mleko", "twarog"]
chemia = ["domestos", "plyn do naczyn", "proszek do prania"]

zakupy_listopad = [nabial, chemia]

zakupy_grudzien = copy.deepcopy(zakupy_listopad)
zakupy_styczen = copy.deepcopy(zakupy_listopad)

zakupy_grudzien[0].append("maka")

print(f"Zakupy listopad {zakupy_listopad}")
print(f"Zakupy grudzien {zakupy_grudzien}")
print(f"Zakupy styczen {zakupy_styczen}")