#Programa para analizar datos del estudiante
import os
os.system("cls")

# Variable que digite la cantidad de estudiantes
cantidad=int(input("Digite la cantidad de estudiantes: "))
# Variables acomuladoras
nombre=[]
nota1=[]
nota2=[]
nota3=[]
promedio=[]
estado=[]

# Función para ingresar los datos de estudiantes 
for i in range(0, cantidad, 1):
    try:
        nombre.append(input("Nombre del estudiante #"+str(i+1)))
        nota1.append(float(input("Digite la nota 1: ")))
        nota2.append(float(input("Digite la nota 2: ")))
        nota3.append(float(input("Digite la nota 3: ")))
        promedio.append((nota1[i]+nota2[i]+nota3[i])/3)
    except ValueError:
        print("Error: Las notas deben ser números válidos.")



for i in promedio:
    
    if(i<70):
        estado.append("Reprobado")
    else:
        estado.append("Aprobado")

for g in range (0,cantidad,1):
    print(f"El estudiante "+nombre[g]+" "+estado[g]+" con un promerio de "+promedio[g]) 