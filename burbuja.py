arreglo = [23,6,4,3,54,54,34]
n = len(arreglo)
contador_de_intercambios=0
print(arreglo) ##Arreglo no ordenado
intercambio = True;
while (intercambio):
    intercambio = False
    for i in range(1,n):
        if arreglo[i-1]>arreglo[i]:
            arreglo[i-1],arreglo[i] = arreglo[i],arreglo[i-1]
            intercambio = True
            contador_de_intercambios+=1
    n-=1
print(arreglo) ##Arreglo ordenado