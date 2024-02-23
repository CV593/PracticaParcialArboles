# Primera Serie
# Diferenciar una lista y un dicionario y de un ejemplo
    #Lista: Coleccion mutable ordenada de elementos
list = [1,2,3,4,5,6]
    #Diccionario: coleccion no ordenada pero tambien es mutable
dic = {
    'clave1': 1,
    'clave2': 2,
    'clave3': 3,
    'clave4': 4,
    'clave5': 5
}

#Como funciona un ciclo for
    #se ejecuta un numero limitada de veces
for num in list:
    print(num)

#Diferencia entre una funcion y una variable
n1 = 1
n2 = 2
def suma(n1, n2):
    return  n1 + n2
#se manda a llamar la funcion
suma(n1,n2)
# las funciones se pueden llamar varias veces con varias variables ya que son
# reutilizables y una variable es una forma de almacenar datos

# Github es una plataforma de desarrollo colaborativa


#escriba una funcion en python que reciba una lista como parametro
def sum_lista(list):
    sum = 0
    for e in list:
        sum += e
    return sum
print(f"La lista es {list}")
print(f"Su suma es {sum_lista(list)}")


# Programa que pide una lista de números 
# y luego imprime la suma de los números pares de la lista

entrada = input("Ingrese los numeros de la lista (separados por espacio): ")
numeros = [int(numero) for numero in entrada.split()]
def sumar_pares(lista):
    suma = 0
    for numero in lista:
        if numero % 2 == 0:
            suma += numero
    return suma

print(f"La lista es {numeros}")
print(f"La suma de los números pares es {sumar_pares(numeros)}")
