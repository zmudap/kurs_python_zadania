import datetime
import time
import math

try:
    ile_sekund = int(input("Podaj ile sekund ma zapisać do pliku program: "))

    with open("logs.txt", "w") as f:
        for sekunda in range(ile_sekund):
            f.write(str(sekunda)
                    + "|" + str(datetime.date.today().day)
                    + " " + str(datetime.datetime.now().strftime("%b"))
                    + " " + str(datetime.date.today().year)
                    + "|" + str(time.strftime("%H:%M:%S", time.localtime()))
                    + "|" + str(math.trunc(time.time())) + "\n")
            time.sleep(1)

except ValueError:
    print("Miałeś podać liczbę sekund!!!")