import random

def main():
    print("¡Bienvenido al Sistema de Reservas de FastFast Airlines!")
    
    #user
    print("\n** Información del Usuario **")
    titulo = input("Ingrese su título (Sr. o Sra.): ").capitalize()
    nombre = input("Ingrese su nombre: ").capitalize()
    apellido = input("Ingrese su apellido: ").capitalize()
    
    nombre_completo = f"{titulo} {nombre} {apellido}"
    print(f"\n{nombre_completo}, ¡Bienvenido a FastFast Airlines!")
    
    #vuelo
    print("\n** Selección de Vuelo **")
    ciudades = ["Medellín", "Bogotá", "Cartagena"]
    
    print("\nCiudades disponibles:")
    for i, ciudad in enumerate(ciudades, 1):
        print(f"{i}. {ciudad}")
    
    origen = int(input("\nSeleccione el número de la ciudad de origen: "))
    while origen < 1 or origen > 3:
        print("Opción inválida. Por favor seleccione 1, 2 o 3.")
        origen = int(input("Seleccione el número de la ciudad de origen: "))
    ciudad_origen = ciudades[origen-1]
    
    destino = int(input("Seleccione el número de la ciudad de destino: "))
    while destino < 1 or destino > 3 or destino == origen:
        if destino == origen:
            print("El destino no puede ser igual al origen. Por favor seleccione otra ciudad.")
        else:
            print("Opción inválida. Por favor seleccione 1, 2 o 3.")
        destino = int(input("Seleccione el número de la ciudad de destino: "))
    ciudad_destino = ciudades[destino-1]
    
    #distancia
    if (ciudad_origen == "Medellín" and ciudad_destino == "Bogotá") or (ciudad_origen == "Bogotá" and ciudad_destino == "Medellín"):
        distancia = 240
    elif (ciudad_origen == "Medellín" and ciudad_destino == "Cartagena") or (ciudad_origen == "Cartagena" and ciudad_destino == "Medellín"):
        distancia = 461
    elif (ciudad_origen == "Bogotá" and ciudad_destino == "Cartagena") or (ciudad_origen == "Cartagena" and ciudad_destino == "Bogotá"):
        distancia = 657
    else:
        distancia = 0
    
    # Fecha del vuelo
    dia_semana = input("\nIngrese el día de la semana que desea viajar (ej. lunes): ").lower()
    while dia_semana not in ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes", "sábado", "sabado", "domingo"]:
        print("Día inválido. Por favor ingrese un día válido (ej. lunes, martes, etc.)")
        dia_semana = input("Ingrese el día de la semana que desea viajar: ").lower()
    
    dia_mes = int(input("Ingrese el día del mes (1-30): "))
    while dia_mes < 1 or dia_mes > 30:
        print("Día inválido. Por favor ingrese un número entre 1 y 30.")
        dia_mes = int(input("Ingrese el día del mes (1-30): "))
    
    # Calcular precio
    if distancia < 400:
        if dia_semana in ["lunes", "martes", "miércoles", "miercoles", "jueves"]:
            precio = 79900
        else:
            precio = 119900
    else:
        if dia_semana in ["lunes", "martes", "miércoles", "miercoles", "jueves"]:
            precio = 156900
        else:
            precio = 213000
    
    # 3. Asignación de asiento
    print("\n** Asignación de Asiento **")
    preferencia = input("¿Prefiere asiento en el pasillo, ventana o no tiene preferencia? (pasillo/ventana/nada): ").lower()
    while preferencia not in ["pasillo", "ventana", "nada"]:
        print("Opción inválida. Por favor ingrese 'pasillo', 'ventana' o 'nada'.")
        preferencia = input("¿Prefiere asiento en el pasillo, ventana o no tiene preferencia?: ").lower()
    
    if preferencia == "pasillo":
        letra = "C"
    elif preferencia == "ventana":
        letra = "A"
    else:
        letra = "B"
    
    numero_asiento = random.randint(1, 29)
    asiento = f"{numero_asiento}{letra}"
    
    # 4. Salida
    print("\n** Resumen de su Reserva **")
    print(f"Nombre del pasajero: {nombre_completo}")
    print(f"Origen: {ciudad_origen}")
    print(f"Destino: {ciudad_destino}")
    print(f"Fecha de vuelo: {dia_semana.capitalize()} {dia_mes} del mes")
    print(f"Precio del boleto: ${precio:,}")
    print(f"Asiento asignado: {asiento}")
    print("\n¡Gracias por elegir FastFast Airlines! ¡Buen viaje!")

if __name__ == "__main__":
    main()