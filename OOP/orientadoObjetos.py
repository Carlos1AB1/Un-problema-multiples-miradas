# --- Paradigma OOP ---
class GestorTareas:
    def __init__(self):   # ✅ constructor con doble guion bajo
        self.tareas = []  # Inicializamos la lista vacía de tareas

    def agregar(self, tarea):
        self.tareas.append(tarea)  # Agrega la tarea a la lista

    def mostrar(self):
        for i, t in enumerate(self.tareas, 1):
            print(f"{i}. {t}")  # Muestra las tareas numeradas desde 1

    def eliminar(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)  # Elimina la tarea en la posición indicada

# Uso:
gestor = GestorTareas()
gestor.agregar("Leer un libro")
gestor.agregar("Practicar Python")
gestor.agregar("Practicar OCL")
gestor.mostrar()
gestor.eliminar(2)  # Elimina la tercera tarea (índice 2)
gestor.mostrar()
# --- Paradigma OOP ---