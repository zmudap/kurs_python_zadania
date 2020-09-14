import random
lista_liczb = []

try:
    ile_liczb = int(input("Podaj ile losowych libcz ma wygenerować program: "))

    for liczba in range(ile_liczb):
        lista_liczb.append(round(random.random(), 5))

    lista_liczb.sort()

    with open("percent.txt", "w") as f:
        for liczba1 in lista_liczb:
            f.write(str(liczba1) + " ; " + str("{:.0%}".format(liczba1)) + "\n")

    print("Wygenerowane liczby i ich wartość procentowa podane są w pliku percent.txt")

except ValueError:
    print("MIAŁEŚ PODAĆ ILOŚĆ LICZB")


