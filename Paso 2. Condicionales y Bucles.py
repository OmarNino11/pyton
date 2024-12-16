numero =  int(input("elige tu numero "))

if numero % 2 == 0:
    print(f"el numero {numero} es par")
else:
    print(f"el numero {numero} es inpar")


numeros = [1,2,3,4,5,6]

print("\nCuadrados de los números en la lista:")

for num in numeros:
    print(f"el cuadrado de {num} es {num **2}")


while True:
    numero_positivo = int(input("\nIntroducve un numero positivo "))
    if numero_positivo > 0:
        print(f"¡Has ingresado un número positivo: {numero_positivo}!")
        break
    else: 
        print(f"¡Has ingresado un número negativo: {numero_positivo}!")