#Calculadora 
import time


time.sleep(1)

time.sleep(0)

numero1 = int(input("primer número: "))
numero2 = int(input(f"segundo número: "))
print(f"De acuerdo, has escogido el {numero1} y el {numero2}")
time.sleep(1)

simbolo = input(f" (Escribe el numero)\n 1 Sumar\n 2 Restar\n 3 Multiplicar\n 4 Dividir\n 5 salir")

if simbolo == '1' or simbolo == "1":
    print(f"{numero1} + {numero2} =",(numero1+numero2))
elif simbolo == '2' or simbolo == "2":
    print(f"{numero1} - {numero2} =",(numero1-numero2))
elif simbolo == '3' or simbolo == "3":
    print(f"{numero1} * {numero2} =",(numero1*numero2))
elif simbolo == '4' or simbolo == "4":
    print(f"{numero1} / {numero2} =",(numero1/numero2))
elif simbolo == '5' or simbolo == "5":
    print(f"fin")
    
else:
    print(f"No has escrito ninguna letra correcta\nS|s para sumar R|r para restar M|m para multiplicar o D|d para dividir")