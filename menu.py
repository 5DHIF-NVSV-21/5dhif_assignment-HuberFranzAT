import math
import os

class Functions:
    
    def __init__(self):
        pass
    
    def fibonacci(self, num1, num2, current, end):
        current += 1
        erg = num1 + num2
        num1, num2 = num2, erg
        if current < end:
            erg = self.fibonacci(num1, num2, current, end)
        return erg

    def binaer_to_decimal(self):
        inputBin = input("Binaer: ")
        inputBin = inputBin[::-1]
        dez = 0
        for i in range(0, len(inputBin)):
            dez += math.pow(2,i) * int(inputBin[i])
            pass
        pass
        print(f'Dezimal: {int(dez)}')

    def decimal_to_binaer(self):
        inputDec = int(input("Dezimal: "))
        check = True
        binaer = ""
        while check:
            binaer += str((inputDec % 2))
            inputDec = int(inputDec / 2)
            if inputDec == 0:
                check = False
                pass
            pass
        print(f'Binaer: {binaer[::-1]}')
        pass

    def primnumbers(self):
        inputNum = int(input("Eine Zahl eingeben: "))
        for i in range(2 ,int(math.sqrt(inputNum))+1):
            if inputNum % i == 0:
                print(f'Die Zahl {inputNum} ist keine Primzahl')
                return
            pass
        print(f'Die Zahl {inputNum} ist eine Primzahl')
        pass

    def polish_notation(self):
        inputCalc = input("Umgekehrte Polnische Notation (mit Leerzeichen getrennt): ")
        #inputCalc = inputCalc[::-1]
        temp = inputCalc.split(" ")
        erg = 0
        i = 0
        func = Functions()

        while i < len(temp):
            if temp[i] == "+":
                erg = float(temp[i-2]) + float(temp[i-1])
                temp = func.get_new_temp(temp, i, erg)
                i = -1
                pass
            elif temp[i] == "-":
                erg = float(temp[i-2]) - float(temp[i-1])
                temp = func.get_new_temp(temp, i, erg)
                i = -1
                pass
            elif temp[i] == "*":
                erg = float(temp[i-2]) * float(temp[i-1])
                temp = func.get_new_temp(temp, i, erg)
                i = -1
                pass
            elif temp[i] == "/":
                erg = float(temp[i-2]) / float(temp[i-1])
                temp = func. get_new_temp(temp, i, erg)
                i = -1
                pass
            i += 1

            if len(temp) == 1:
                print(f'Ergebnis: {erg}')
                return
            pass
        pass
    
    def write_on_file(self):
        file = open("menu.txt", "w")
        inputStr = input("Text: ")
        file.write(inputStr)
        file.close()
        pass

    def open_file(self):
        os.startfile("menu.txt")
        pass

    def get_new_temp(self, temp, index, erg):
        temp[index] = str(erg)
        temp2 = temp[0 : index-2]
        return temp2 + temp[index:]
        pass
    pass


if __name__ == "__main__":
    checker = True
    while checker:
        print("\nMenu:")
        print("[1] Fibonacci Zahlen\n[2] Binaer zu Dezimal\n[3] Primzahlen\n[4] Dezimal zu Binaer\n" +
              "[5] Umgekehrte Polnische Notation\n[6] Write something on a .txt\n[7] Open the .txt\n[8] Exit")
        menuPunkt = input("\nMenu-Punkt: ");

        func = Functions()

        try:
            if menuPunkt == "1":
                inputNum = input("Die wievielte Fibonacci Zahl: ")
                fibonacciZahl = func.fibonacci(0, 1, 0, int(inputNum)-1)
                print(f'Fibonacci: {fibonacciZahl}')
                pass
            elif menuPunkt == "2":
                func.binaer_to_decimal()
                pass
            elif menuPunkt == "3":
                func.primnumbers()
                pass
            elif menuPunkt == "4":
                func.decimal_to_binaer()
                pass
            elif menuPunkt == "5":
                func.polish_notation()
                pass
            elif menuPunkt == "6":
                func.write_on_file()
                pass
            elif menuPunkt == "7":
                func.open_file()
                pass
            elif menuPunkt == "8":
                checker = False
                pass
            else:
                pass
        except:
            print("\nWrong input type\n")
            pass        
        pass
    pass