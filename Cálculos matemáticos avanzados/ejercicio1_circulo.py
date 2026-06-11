import math
import os
# Limpiar la consola
os.system('cls' if os.name == 'nt' else 'clear')

# Solicitar el radio del círculo al usuario
radio = float(input("Ingrese el radio del círculo: "))


# Calcular área del círculo: area = pi * radio²
# Usamos math.ceil para redondear hacia arriba el valor de pi y el resultado del área
area = math.ceil(math.ceil(math.pi) * math.ceil(math.pow(radio, 2)))


# Calcular perímetro (circunferencia): Perimetro = 2 * pi * radio
perimetro = 2 * math.ceil(math.ceil(math.pi) * radio)

# Redondear a 2 decimales
area_redondeada = round(area, 2)
perimetro_redondeado = round(perimetro, 2)

# Determinar si el área es mayor a 100
es_mayor_100 = area_redondeada > 100

# Mostrar resultados

print(f"Radio del círculo: {radio}")

print(f"Área del círculo: {area_redondeada:.2f} unidades²")
print(f"Perímetro (Circunferencia): {perimetro_redondeado:.2f} unidades")


if es_mayor_100:
    print(f"✓ El área ({area_redondeada:.2f}) es mayor a 100")
else:
    print(f"✗ El área ({area_redondeada:.2f}) no es mayor a 100")

print("-"*50)

