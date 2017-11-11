# 10. zamiana temperatury
# #     wejscie: "35C" "100F"
# #     wyjście "Temperatura w {typ} to {xxx} stopni"
# #     C = (F - 32) * (5/9)
# #     F = C * (9 / 5) + 32


temp_input = str(input("Podaj temperaturę wraz z symbolem jednostki [C lub F] \n"))
temp_input = temp_input.upper()

jednostka = temp_input[-1]
if jednostka == "C":
    typ = "F"
elif jednostka == "F":
    typ = "C"
else:
    print("Błedna jednostka")
    exit(666)

temperatura = int(temp_input[:-1])

if jednostka == "C":
    temp_F_out = round(temperatura * (9 / 5) + 32, 1)
    print(f"Temperatura w {typ} to " + str(temp_F_out) + " stopni")
elif jednostka == "F":
    temp_C_out = round((temperatura - 32) * (5 / 9), 1)
    print(f"Temperatura w {typ} to " + str(temp_C_out) + " stopni")


#
# temperatura_C = "35C"
# temperatura_F = "100F"
# typ_c = "stopniach C"
# typ_f = "stopniach F"
# temp_liczba_c = int(temperatura_C[:-1])
# temp_liczba_f = int(temperatura_F[:-1])

# z_F_na_C = (temp_liczba_f - 32) * (5 / 9)
# wart_round_1 = round(z_F_na_C, 1)
# print(f"Temperatura w {typ_c} to " + str(wart_round_1))
#
# z_C_na_F = temp_liczba_c * (9 / 5) + 32
# wart_round_2 = round(z_C_na_F, 1)
# print(f"Temperatura w {typ_f} to " + str(wart_round_2))