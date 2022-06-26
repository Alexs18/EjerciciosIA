vector= []
#Se inicializa las variables a usar
suma=0
suma1=0
n=int(input("Ingrese el tamaño del vector: "))
#Creacion ciclo for
for x in range(n):
    valor=int(input("Ingrese un número"))
    vector.append(valor)
#Condición if
if x % 2 == 0:
    suma=suma+valor
    promedio=suma/5
else:
    suma1=suma1+valor
    promedio1=suma1/5
#Impresión
print("La suma de los numeros pares del arreglo es:",suma)
print("El promedio de los numeros pares del arreglo es:",promedio)
print("La suma de los numeros impares del arreglo es:",suma1)
print("El promedio de los numeros impares del arreglo es:",promedio1)