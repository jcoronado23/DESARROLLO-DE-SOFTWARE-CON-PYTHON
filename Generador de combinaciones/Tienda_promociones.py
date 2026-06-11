import itertools
import os

# Lista de productos
productos = ["Pan", "Café", "Leche", "Queso"]

# Generar combinaciones de 2 productos
combinaciones_2 = list(itertools.combinations(productos, 2))

# Generar combinaciones de 3 productos
combinaciones_3 = list(itertools.combinations(productos, 3))

# Limpiar la consola
os.system('cls' if os.name == 'nt' else 'clear')

# Mostrar título
print('<<  Welcome to the Promotion Generator  >>\n')
# Mostrar combinaciones de 2 productos
print("\nCombinaciones de 2 productos en promoción\n")
for combinacion in combinaciones_2:
    print(combinacion)


# Mostrar combinaciones de 3 productos
print("\nCombinaciones de 3 productos en promoción\n")
for combinacion in combinaciones_3:
    print(combinacion)

# Mostrar cantidad de combinaciones de 2 productos
print(f"\nTotal de promociones de 2 productos: {len(combinaciones_2)}")
# Mostrar cantidad de combinaciones de 3 productos
print(f"Total de promociones de 3 productos: {len(combinaciones_3)}")

#generar total de 2 y 3 productos
total = len(combinaciones_2) + len(combinaciones_3)
print(f'Total de promociones: {total}\n')