def simular_desintegracion_orbital():
    print("Simulación de Desintegración Orbital de un Satélite")
    print("--------------------------------------------------\n")
    
    # 1. Solicitud de datos de entrada
    try:
        altitud_inicial = float(input("Ingrese la altitud inicial del satélite (km): "))
        coeficiente_arrastre = float(input("Ingrese el coeficiente de arrastre inicial (ej. 0.01): "))
        altitud_minima = float(input("Ingrese la altitud mínima de seguridad (km): "))
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")
        return
    
    # Validación de valores de entrada
    if altitud_inicial <= 0 or coeficiente_arrastre <= 0 or altitud_minima < 0:
        print("Error: Todos los valores deben ser positivos.")
        return
    if altitud_inicial <= altitud_minima:
        print("Error: La altitud inicial debe ser mayor que la altitud mínima de seguridad.")
        return
    
    # 2. Simulación de órbitas
    altitud_actual = altitud_inicial
    orbitas_completadas = 0
    estabilizado = False
    
    print("\nIniciando simulación...")
    print(f"Órbita 0: Altitud = {altitud_actual:.2f} km")
    
    while True:
        orbitas_completadas += 1
        
        # Calcular pérdida de altitud
        altitud_perdida = coeficiente_arrastre * altitud_actual
        altitud_actual -= altitud_perdida
        
        # Aumentar coeficiente de arrastre
        coeficiente_arrastre += 0.0001
        
        # Mostrar progreso cada 100 órbitas o cuando esté cerca del final
        if orbitas_completadas % 100 == 0 or altitud_actual < altitud_minima + 50:
            print(f"Órbita {orbitas_completadas}: Altitud = {altitud_actual:.2f} km, Pérdida = {altitud_perdida:.4f} km")
        
        # Condiciones de terminación
        if altitud_actual <= altitud_minima:
            break
            
        if altitud_perdida < 0.001:  # Umbral de estabilización
            estabilizado = True
            break
    
    # 3. Mostrar resultados
    print("\n--- Resultados de la Simulación ---")
    print(f"Órbitas completadas: {orbitas_completadas}")
    print(f"Altitud final: {altitud_actual:.2f} km")
    
    if estabilizado:
        print("\nEl satélite se ha estabilizado en órbita.")
        print(f"Altitud de estabilización: {altitud_actual:.2f} km")
    else:
        print("\n¡El satélite ha reingresado en la atmósfera terrestre!")
        print(f"Altitud de reingreso: {altitud_minima} km")
    
    print("\nSimulación completada.")

if __name__ == "__main__":
    simular_desintegracion_orbital()