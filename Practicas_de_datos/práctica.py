entrada = "  usuario: Diego | edad: 28 | pais: CR  "

# 1. Limpiar espacios
entrada = entrada.strip()

# 2. Extraer nombre usando slicing
inicio_nombre = entrada.find(":") + 2
fin_nombre = entrada.find("|")
nombre = entrada[inicio_nombre:fin_nombre].strip()

# 3. Extraer edad usando slicing
inicio_edad = entrada.find("edad:") + 6
fin_edad = entrada.find("|", inicio_edad)
edad = entrada[inicio_edad:fin_edad].strip()

# 4. Resultado profesional
print('Desarmando un string')
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")