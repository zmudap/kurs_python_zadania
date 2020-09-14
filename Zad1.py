import math
pi = math.pi


def prostokat(a, *b):
    if a > 0 and b > 0:
        return a*b
    if a <= 0 or b <= 0:
        return print("Podałeś  liczby nierzeczywiste!")


def kwadrat(a):
    if a > 0:
        return a*a
    if a <= 0:
        return print("Podałeś złą szerokość kwadratu!")


def kolo(r):
    if r > 0:
        return 2*pi*r
    if r <= 0:
        return print("Podałeś zły promień koła!")


def trojkat(a, h):
    if a > 0 and h > 0:
        return a*h/2
    if a <= 0 or h < 0:
        return print("Podałeś złe wartości trójkąta!")


def trapez(a,b,h):
    if a > 0 and b > 0 and h > 0:
        return (a+b)*h/2
    if a <= 0 or b <= 0 or h <= 0:
        return print("Podałeś złe wartości trapeza")


try:
    print("Wpisz z listy dla jakiej figury bedzie liczone pole:\n"
          "prostokat, kwadrat, kolo, trojkat, trapez")
    figura = input()

    if figura == "prostokat":
        a = float(input("Podaj pierwszą szerokość prostokata "))
        b = float(input("Podaj drugą szerokość prostokąta "))
        print('Pole figury "'+str(figura)+'" o podanych wartościach wynosi '+str(prostokat(a, b)))

    elif figura == "kwadrat":
        a = float(input("Podaj szerokość kwadratu "))
        print('Pole figury "' + str(figura) + '" o podanych wartościach wynosi ' + str(kwadrat(a)))

    elif figura == "kolo":
        r = float(input("Podaj promień koła "))
        print('Pole figury "' + str(figura) + '" o podanych wartościach wynosi ' + str(kolo(r)))

    elif figura == "trojkat":
        a = float(input("Podaj podstawę trójkąta "))
        h = float(input("Podaj wysokość trójkąta "))
        print('Pole figury "' + str(figura) + '" o podanych wartościach wynosi ' + str(trojkat(a, h)))

    elif figura == "trapez":
        a = float(input("Podaj pierwsza podstawę trapezu "))
        b = float(input("Podaj drugą podstawę trapezu "))
        h = float(input("Podaj wysokość trapezu "))
        print('Pole figury "' + str(figura) + '" o podanych wartościach wynosi ' + str(trapez(a, b, h)))

    else:
        print("Wpisałeś złą nazwę z listy. Spróbuj jeszcze raz :)")

except ValueError:
    print("MIAŁEŚ PODAĆ ILOŚĆ LICZBĘ!")