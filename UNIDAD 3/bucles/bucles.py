'''''
# Definimos el menú de comida como un diccionario
menu = {
    1: {"nombre": "Pizza", "ingredientes": ["Masa", "Salsa de tomate", "Queso", "Pepperoni"]},
    2: {"nombre": "Hamburguesa", "ingredientes": ["Pan", "Carne de res", "Lechuga", "Tomate", "Queso"]},
    3: {"nombre": "Ensalada César", "ingredientes": ["Lechuga", "Pollo", "Crutones", "Queso parmesano", "Aderezo César"]},
    4: {"nombre": "Sushi", "ingredientes": ["Arroz", "Alga nori", "Pescado", "Aguacate", "Salsa de soja"]},
    5: {"nombre": "Tacos", "ingredientes": ["Tortilla", "Carne", "Cebolla", "Cilantro", "Salsa"]}
}

def mostrar_menu():
    print("\nMenú de Comida:")
    for key, value in menu.items():
        print(f"{key}. {value['nombre']}")
    print("E. Salir")

def mostrar_ingredientes(plato):
    print(f"\nPlato: {plato['nombre']}")
    print("Ingredientes:")
    for ingrediente in plato['ingredientes']:
        print(f"- {ingrediente}")

while True:
    mostrar_menu()
    opcion = input("\nIngresa el número del plato que deseas ver (o 'E' para salir): ").strip().upper()

    if opcion == "E":
        print("¡Gracias por usar el menú! ¡Hasta luego!")
        break  

    try:
        opcion = int(opcion) 
        if opcion in menu:
            mostrar_ingredientes(menu[opcion])
        else:
            print("Opción no válida. Por favor, ingresa un número del menú.")
    except ValueError:
        print("Por favor, ingresa un número válido o 'E' para salir.")
'''''
'''
# Inicializamos la variable contador
contador = 0

# Definimos el valor máximo hasta el cual queremos contar
valor_maximo = 10

# Usamos un bucle while para contar hasta el valor máximo
while contador <= valor_maximo:
    print(contador)
    contador += 1  # Incrementamos el contador en 1 en cada iteración

'''
'''
num = int(input(print("ingese un número: ")))
cont = 1
print("Tabla del ", num)
while cont <= 10:
    print(f"{num} x {cont} = {num*cont}")
    cont += 1
'''
# Definir una lista de frutas
lista_frutas = ["Manzana", "Banana", "Cereza", "Maracuyá"]

# Utilizar un ciclo for para imprimir cada fruta en la lista
for fruta in lista_frutas:
    print(fruta)
    
for indice in range(4):
    print(lista_frutas[indice])