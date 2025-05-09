import random

# Diccionario de distancias entre ciudades (en km)
distancias = {
    ('Medellín', 'Bogotá'): 240,
    ('Medellín', 'Cartagena'): 461,
    ('Bogotá', 'Medellín'): 240,
    ('Bogotá', 'Cartagena'): 657,
    ('Cartagena', 'Medellín'): 461,
    ('Cartagena', 'Bogotá'): 657
}

# Precios según distancia y día
precios = {
    'corta': {'semana': 79900, 'fin_semana': 119900},
    'larga': {'semana': 156900, 'fin_semana': 213000}
}

# Mapeo de preferencias de asiento
asientos_preferencia = {
    'pasillo': 'C',
    'ventana': 'A',
    'no': 'B'
}

# Días de semana y fin de semana
dias_semana = ['lunes', 'martes', 'miércoles', 'jueves']
dias_fin_semana = ['viernes', 'sábado', 'domingo']

def obtener_precio(distancia_km, dia_semana):
    """Calcula el precio del boleto según distancia y día"""
    if distancia_km < 400:
        tipo_tarifa = 'corta'
    else:
        tipo_tarifa = 'larga'
    
    if dia_semana.lower() in dias_semana:
        return precios[tipo_tarifa]['semana']
    else:
        return precios[tipo_tarifa]['fin_semana']

def asignar_asiento(preferencia):
    """Asigna un asiento aleatorio según preferencia"""
    numero = random.randint(1, 29)
    letra = asientos_preferencia.get(preferencia.lower(), 'B')
    return f"{numero}{letra}"

def main():
    # 1. Información del usuario
    print("Bienvenido al Sistema de Reservas de FastFast Airlines\n")
    
    titulo = input("¿Es usted señor o señora? (Sr./Sra.): ").capitalize()
    nombre = input("Introduce tu nombre: ").capitalize()
    apellido = input("Introduce tu apellido: ").capitalize()
    
    nombre_completo = f"{titulo} {nombre} {apellido}"
    print(f"\n{nombre_completo}, ¡Bienvenido a FastFast Airlines!\n")
    
    # 2. Selección de vuelo
    ciudades = ['Medellín', 'Bogotá', 'Cartagena']
    
    print("Por favor ingrese los detalles de su vuelo:")
    origen = input(f"Ingresa tu origen ({', '.join(ciudades)}): ").capitalize()
    while origen not in ciudades:
        print("Ciudad no válida. Por favor elija entre las opciones.")
        origen = input(f"Ingresa tu origen ({', '.join(ciudades)}): ").capitalize()
    
    destino = input(f"Ingresa tu destino ({', '.join(ciudades)}): ").capitalize()
    while destino not in ciudades or destino == origen:
        if destino == origen:
            print("El origen y destino no pueden ser iguales.")
        else:
            print("Ciudad no válida. Por favor elija entre las opciones.")
        destino = input(f"Ingresa tu destino ({', '.join(ciudades)}): ").capitalize()
    
    dia_semana = input("Ingrese el día de la semana (por ejemplo, lunes): ").lower()
    while dia_semana not in dias_semana + dias_fin_semana:
        print("Día no válido. Por favor ingrese un día de la semana (ej. lunes, martes, etc.)")
        dia_semana = input("Ingrese el día de la semana (por ejemplo, lunes): ").lower()
    
    dia_mes = input("Introduzca el día del mes (1-30): ")
    while not dia_mes.isdigit() or int(dia_mes) < 1 or int(dia_mes) > 30:
        print("Día del mes no válido. Debe ser un número entre 1 y 30.")
        dia_mes = input("Introduzca el día del mes (1-30): ")
    
    # 3. Cálculo de precio
    distancia = distancias.get((origen, destino), 0)
    precio = obtener_precio(distancia, dia_semana)
    
    # 4. Asignación de asiento
    print("\nOpciones de asiento:")
    print("1. Pasillo")
    print("2. Ventana")
    print("3. Sin preferencia")
    opcion_asiento = input("Seleccione su preferencia de asiento (1-3): ")
    
    preferencia = ''
    if opcion_asiento == '1':
        preferencia = 'pasillo'
    elif opcion_asiento == '2':
        preferencia = 'ventana'
    else:
        preferencia = 'no'
    
    asiento = asignar_asiento(preferencia)
    
    # 5. Mostrar resumen
    print("\nResumen de su reserva:")
    print(f"Nombre: {nombre_completo}")
    print(f"Vuelo: {origen} → {destino}")
    print(f"Fecha: {dia_semana.capitalize()} {dia_mes} de [mes]")  # Podrías agregar lógica para el mes si lo deseas
    print(f"Distancia: {distancia} km")
    print(f"Precio del boleto: ${precio:,}")
    print(f"Asiento asignado: {asiento}")
    print("\n¡Gracias por reservar con FastFast Airlines!")

if __name__ == "__main__":
    main()