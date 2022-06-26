# Crear un menú para el usuario
menu = """
1- Ingresar
2- Suma_sueldo
3- Sueldo_max_min
4- Mostrar todo
5- Salir
"""
print(menu)
op = int(input("Ingrese una opción del menú: "))
# Se realizan las operaciones de cada opción
if op == 1:
    nombres=[]
    cargo=[]
    sueldo=[]
    sueld = 0
    n=int(input("Ingrese el numero de trabajadores: "))
for x in range(n):
    nom=input("Ingrese el nombre del trabajador: ")
    nombres.append(nom)
    car=input("Ingrese el cargo: ")
    cargo.append(car)
    suel=int(input("Ingrese el sueldo: "))
    sueldo.append(suel)
    sueld= sueld + suel
    prom=sueld/n
for x in range(n):
    print(nombres[x], cargo[x], sueldo[x])
    op = int(input("Ingrese una opción del menú: "))
if op == 2:
    print("La suma del sueldo total de los trabajadores es: ", sueld)
    print("El promedio del sueldo total de los trabajadores es: ", prom)
    op = int(input("Ingrese una opción del menú: "))
if op == 3:
    mayor = sueldo[0]
for suel in sueldo:
    if suel > mayor:
        mayor=suel
        print("El sueldo máximo es: ", nombres[x], cargo[x], mayor)
        menor = sueldo[0]
for suel in sueldo:
    if suel < menor:
        menor=suel
        print("El sueldo mínimo es: ", nombres[x], cargo[x], menor)
        op = int(input("Ingrese una opción del menú: "))
    if op == 4:
        print("El número de trabajadores son: ", n)
    for x in range(n):
        print(nombres[x], cargo[x], sueldo[x])
        print("La suma del sueldo total de los trabajadores es: ", sueld)
        print("El promedio del sueldo total de los trabajadores es: ", prom)
        print("El sueldo máximo es: " nombres[x], cargo[x], mayor)
        print("El sueldo máximo es: ", nombres[x], cargo[x], mayor)
        print("El sueldo mínimo es: ", nombres[x], cargo[x], menor)
        op = int(input("Ingrese una opción del menú: "))
    if op == 5:
        print("Salir")
    else:
        print("El numero de opción no existe")