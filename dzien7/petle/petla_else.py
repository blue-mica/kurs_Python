for x in range(10):
    if x ** 2 > 100:
        print(f"Kwadrat {x} jest wiekszy od 100")
        break
else:
    print("Zaden kwadrat nie jest wiekszy od 100")

print("tutaj przeksakuje jek wykonam 'break'")