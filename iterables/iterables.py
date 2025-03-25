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

