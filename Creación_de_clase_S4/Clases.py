import math
import os

# Definimos una clase llamada figura, que contiene metodos de calcular_area y calcular_perimetro

class figura:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass
    
# Definimos una clase llamada cono, que hereda de la clase figura, y contiene un metodo para calcular el area y el perimetro del cono
class cono(figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
        
    def calcular_area(self):
        import math
        return math.pi * self.radio * (self.radio + math.sqrt(self.altura**2 + self.radio**2))
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
# Definimos una clase llamada esfera, que hereda de la clase figura, y contiene un metodo para calcular el area y el perimetro del cuadrado
# Esfera no tiene perimétro, pero si volumen. Mejorar programa con base a figuras geométricas.

class esfera(figura):
    # Tiene diferentes atributos, como el lado del cuadrado
    
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 4 * math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


# Creamos una instancia de la clase cono y esfera.
cono1 = cono(5, 10)
esfera1 = esfera(5)


# Limpiamos la consola para una mejor visualización
os.system("cls" if os.name == "nt" else "clear")

#Utilizamos una lista de figuras y recorremos cada objeto llamando a los mismos métodos, sin importar de qué tipo específico sea.
figuras = [cono1, esfera1]
for figura in figuras:
    print("🔹" * 30)
    print(f"Figura: {figura.__class__.__name__}\n")
    print(f"Área: {figura.calcular_area():.2f}")
    print(f"Perímetro: {figura.calcular_perimetro():.2f}\n")
    print("🔹" * 30)
