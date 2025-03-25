'''
lista_canciones = ["Accidentally in love", "I just threw the love of my dreams", "As it was", "Amor eterno", "Humble"]
lista_cantantes = ["counting crows", "weezer", "Harry styles", "Juan gabriel", "kendrik lammar"]

indices = 0
while indice < 5:
    print(f"{lista_canciones{indice}} la interpreta {lista_cantantes{indice}}")
    indice = indice + 1

#con for 

lista_canciones = ["Accidentally in love", "I just threw the love of my dreams", "As it was", "Amor eterno", "Humble"]
lista_cantantes = ["counting crows", "weezer", "Harry styles", "Juan gabriel", "kendrik lammar"]


for indice in range(5):
    print(f"{lista_canciones{indice}} la interpreta {lista_cantantes{indice}}")

for cancion in lista_canciones:
    print(cancion)

#que hace cada uno 

#Tarea, 
# crear una lista vacia
# Llenar esa lista con 100 números aleatorios utilizados un bucle 
'''
'''
#Ejercicio 5

elementos = ["Cobre","Hierro", "Bromo", "Calcio", "Cobre"]
elementos.insert(1,"Cobre")
elementos.insert(3,"Fluor")
elementos.sort()
cantidad_Cobre = elementos.count("Cobre")   
print("Cantidad de Cobre:", cantidad_Cobre)
indice_Hierro = elementos.index("Hierro")
print("Índice de Hierro:", indice_Hierro)

'''
frase = "Los agujeros negros se forman por un proceso de colapso gravitatorio o desmoronamiento hacia adentro de un cuerpo celeste debido al efecto de su propia gravedad. En el centro la materia confluye hacia un punto llamado singularidad. La superficie esférica alrededor de una singularidad que limita la zona donde la materia y la energía ya no pueden escapar se denomina horizonte de sucesos u horizonte de eventos, porque los eventos a un lado de ella no pueden afectar a un observador situado al otro lado"
car_con_espacio = len(frase)
print(car_con_espacio)
lista_palabras = frase.split()
print(lista_palabras)
num_palabras = len(lista_palabras)
print(f"Palabras en la frase: {num_palabras}")
blancos = frase.count(" ")
print(f"Total caracteres en blanco: {blancos}")
car_sin_espacio = car_con_espacio - blancos
print(f"Total caracteres sin espacio: {car_sin_espacio}")
letras_o = frase.lower().count('o')
letras_s = frase.lower().count('s')
print(f"La letra o se repite {letras_o} veces y la s {letras_s} veces.")