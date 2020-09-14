produkty_z_cena = {}
zakupy = input("Podaj liste zakupów odzielonych przecinkiem:\n")
lista_zakupow = set(zakupy.split(","))

for produkt in lista_zakupow:
    cena = input("Prosze podać cenę produktu - "+produkt+": ")
    if cena.isnumeric():
        produkty_z_cena.update({produkt.upper() : int(cena)})
    else:
        produkty_z_cena.update({produkt.upper() : int(0)})

for produkt in produkty_z_cena.keys():
    print(produkt+":", str(produkty_z_cena[produkt]) +" ZŁ")

if sum(produkty_z_cena.values()) >100:
    print("Masz za mało pieniędzy na te zakupy.")
    print("Brakuje Ci " + str(-(100-sum(produkty_z_cena.values()))) + " złotych")
else:
    print("Masz wystarczająco pieniędzy na te zakupy.")
    print("Z 100 złotych zostanie Ci: " + str(100-sum(produkty_z_cena.values())) + " złotych")