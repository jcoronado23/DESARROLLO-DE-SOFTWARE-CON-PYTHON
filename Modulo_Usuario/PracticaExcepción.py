lista = [10, 20, 30]

try:
    indice = int(input("Ingrese índice: "))
    divisor = int(input("Ingrese divisor: "))

    resultado = lista[indice] / divisor
    print("Resultado:", resultado)

except ZeroDivisionError:
    print("El número indicado no se puede dividir por cero.")

except IndexError:
    print("El índice ingresado no existe en la lista.")

except ValueError:
    print("Debe ingresar únicamente números enteros.")