cant_product = int(input("¿Cuántos productos quieres comprar?: "))
stock_inicial = 50
stock_restante = 0
while stock_restante >= 0:
    #
    stock_restante = stock_inicial - cant_product
    #se apregan los :
    print("Compra realizada.Stock restante: {stock_restante} ")
    if stock_restante < 0:
        #se agregan los :
        print("No hay suficientes productos disponibles")
    elif stock_restante == 0:
        print("Inventario agotado")