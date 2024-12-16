#calculadora
def calculadora():
 
    print("Bienvenido a la calculadora basica.")
    print("operaciones disponibles:")
    print("1.suma (+)")
    print("2.resta (-)")
    print("3.multplicacion (*)")
    print("4.division (/)")
    print("5.salir.")

    while True: 
        opcion = input("\nSelecciona una operación (1-5): ")
        if opcion == "5":
         print("saliendo de la calculadora. ¡ADIOS!")
         break
        
        if opcion not in ["1","2","3","4"]:
         print("opcion no valida por favor intente, intente de nuevo.")
         continue
        
        try:
            num1 = float(input("escoge tu primer numero: "))
            num2 = float(input("escoge tu segundo numero: "))
            

        except ValueError:
         print("porfavo escoge valores numericos validos.")
         continue
        
        if opcion == "1":
         resultado = num1 + num2
         print(f"RESULTADO: {num1} + {num2} = {resultado}")

        elif opcion == "2":
         resultado = num1 - num2
         print(f"RESULTADO: {num1} - {num2} = {resultado}")

        elif opcion == "3":
         resultado = num1 * num2
         print(f"RESULTADO: {num1} * {num2} = {resultado}")

        elif opcion == "4":
         if num2 == 0:
            print("error no se puede dividir por 0")
        else:
            resultado = num1 / num2
        print(f"RESULTADO: {num1} / {num2} = {resultado}")

calculadora()


#juego de la adivinanza

import random

def juego_adivinanza():

    print("vienvenido al juego de la adivinanza")
    print("el programa a generado un numero del 1 al 100")
    print("intenta divinarlo")

    numero_secreto = random.randint(1,100)
    intentos =  0

    while True:
        try:

            adivinanza=int(input("ingresa tu numero: "))

            intentos += 1

            if adivinanza < numero_secreto:
                print("el numero es mayor. intenta nuevamente.")
            elif adivinanza > numero_secreto:
                print("el numero es menor. intenta nuevamente.")
            else:
                print(f"¡FELICIDADES! adivinaste el numero {numero_secreto} en {intentos} intentos.")
                return
        except ValueError:
            print("Por favor, ingresa un número válido.")


juego_adivinanza()