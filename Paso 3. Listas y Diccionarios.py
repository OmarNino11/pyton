# Lista de nombres de estudiantes
estudiantes = ["Juan", "María", "Luis", "Ana", "Pedro"]


print("Lista de estudiantes:")
for estudiante in estudiantes:
    print(estudiante)
contactos = {
    "Juan": "juan@example.com",
    "María": "maria@example.com",
    "Luis": "luis@example.com"
}

print("\nInformación de contacto:")
for nombre, correo in contactos.items():
    print(f"Nombre: {nombre}, Correo: {correo}")


lista = []
diccionario = {}

while True:
    print("\n¿Qué deseas hacer?")
    print("1. Agregar un elemento a la lista")
    print("2. Actualizar o agregar un elemento al diccionario")
    print("3. Mostrar lista y diccionario")
    print("4. Salir")
    
    opcion = input("Selecciona una opción (1-4): ")
    
    if opcion == "1":
        # Agregar elemento a la lista
        elemento = input("Ingresa un elemento para la lista: ")
        lista.append(elemento)
        print(f"Elemento '{elemento}' agregado a la lista.")
        
    elif opcion == "2":
        # Agregar o actualizar un elemento en el diccionario
        clave = input("Ingresa la clave (por ejemplo, nombre): ")
        valor = input(f"Ingresa el valor para '{clave}': ")
        diccionario[clave] = valor
        print(f"Elemento '{clave}: {valor}' agregado/actualizado en el diccionario.")
        
    elif opcion == "3":
        # Mostrar lista y diccionario
        print("\nLista actual:", lista)
        print("Diccionario actual:", diccionario)
        
    elif opcion == "4":
        # Salir del bucle
        print("Saliendo del programa. ¡Adiós!")
        break
    
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
