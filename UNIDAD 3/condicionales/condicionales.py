#Ejerciocio 1
'''
envio = 0 
compra = input("ingrese el valor de la compra: ")
compra = int(compra)
if compra >= 100000:
   envio = 0
total = compra + envio
print(f"El total de la compra es {total}")

'''
#Ejercicio 2

'''''
num = int(input("Ingrese un número entero: "))
residuo = num % 2
if residuo != 0:
   print(f"{num} es impar")
else
   print(f"{num} es par")

nota = int(input("Ingrese la nota: "))

'''

#condicional simple: si al solicitarte  el número de telefono a una persona y el # número de digitos es diferente a 10, imprimir enpantalla: "no es valido"
'''
numero = input("Ingrese el número telefonico: ")
for digito in numero:
    print(digito)
    contador = contador + 1

if contador !=10:
    print("¡numero no valido...!")

print(numero)

'''
#problema3 condicional doble
'''
cuenta =float(input("Ingrese la cuenta a pagar: "))
sexo = input("ingrese el sexo del niño: ")

if sexo == "niña":
   total = cuenta - 50
elif sexo == "niño":
   total = cuenta -30

'''
print("S. Suma\nR. Resta\nD. Division\nM. Multiplicacion ")