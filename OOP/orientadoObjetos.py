# Ejemplo básico de Programación Orientada a Objetos en Python

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# Herencia
class Estudiante(Persona):
    def __init__(self, nombre, edad, universidad):
        super().__init__(nombre, edad)
        self.universidad = universidad

    def saludar(self):
        return f"Hola, soy {self.nombre}, estudio en {self.universidad}."

# Polimorfismo
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def saludar(self):
        return f"Hola, soy el profesor {self.nombre} y enseño {self.materia}."

# Uso de las clases
persona = Persona("Juan", 30)
estudiante = Estudiante("Ana", 20, "Universidad Nacional")
profesor = Profesor("Carlos", 45, "Matemáticas")

print(persona.saludar())
print(estudiante.saludar())
print(profesor.saludar())