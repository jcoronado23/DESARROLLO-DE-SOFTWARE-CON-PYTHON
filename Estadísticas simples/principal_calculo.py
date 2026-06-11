    # Llamando a la función de media
from calculo import calcular_estadisticas, determinar_variabilidad, notas
import os

# Limpiar la consola
os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    # Calcular las estadísticas
    promedio, mediana, moda, desviacion_estandar = calcular_estadisticas(notas)


# Título del programa
    print("🇨🇷🟰🟰🟰 ESTADISTICA SIMPLES DE NOTAS🟰🟰🟰  🇨🇷\n")
    # Imprimir los resultados
    print(f"Promedio: {promedio:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {moda}")
    print(f"Desviación estándar: {desviacion_estandar:.2f}")

    # Determinar la variabilidad
    resultado_variabilidad = determinar_variabilidad(desviacion_estandar)
    print(resultado_variabilidad)