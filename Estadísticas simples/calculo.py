import statistics

# Notas de los estudiantes
notas = [85, 90, 78, 92, 88, 76, 95]

# Función para calcular las estadísticas (promedio, mediana, moda, desviación estándar)
def calcular_estadisticas(notas):
    promedio = statistics.mean(notas)
    mediana = statistics.median(notas)
    moda = statistics.mode(notas)
    desviacion_estandar = statistics.stdev(notas)
    
    return promedio, mediana, moda, desviacion_estandar

# Función para determinar la variabilidad del grupo(si la desviación estándar es mayor a 8)
def determinar_variabilidad(desviacion_estandar):
    if desviacion_estandar > 8:
        return "El grupo tiene alta variabilidad."
    else:
        return "El grupo tiene baja variabilidad.\n"
    
