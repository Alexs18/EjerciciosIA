# Se pide los valores de Talla y peso
talla=float(input("Escriba su talla: "))
peso=float(input("Escriba su peso: "))
#Se crea la función
def calculoimc(talla,peso):
    return peso/talla**2
#Validación mediante una función
def condicion(IMC):
    if IMC < 18.5:
        return "Bajo peso"
    elif IMC >= 18.5 and IMC <=24.9:
        return "Normal"
    elif IMC >= 25 and IMC <=29.9:
        return "Sobrepeso"
    elif IMC >= 30 and IMC <=34.9:
        return "Obesidad grado I"
    elif IMC >= 35 and IMC <=39.9:
        return "Obesidad grado II"
    elif IMC >= 40:
        return "Obesidad grado III"
#Imprimir
print("Su IMC es:",calculoimc(talla,peso))
print("Su nivel de peso es:", condicion(calculoimc(talla,peso)))