numbers = []

while True:
    value = input("Proszę podać liczbę ")
    if value.isnumeric():
        numbers.append(value)
    elif value == "exit":
        for number in numbers:
            print(number)
        break
    else:
        print("Podałeś " +str(len(numbers))+" liczb. Dalej się bawię")
        continue


