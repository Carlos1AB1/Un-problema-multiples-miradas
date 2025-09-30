class ToDoList:
    def __init__(self):
        # La lista donde guardaremos las tareas (solo texto)
        self.tareas = []

    def agregar(self, texto):
        # Agrega una nueva tarea al final de la lista
        self.tareas.append(texto)

    def mostrar(self):
        # Si no hay tareas, avisamos
        if not self.tareas:
            print("No hay tareas.")
        else:
            # Enumeramos desde 1 (más natural que empezar en 0)
            for i, t in enumerate(self.tareas, start=1):
                print(f"{i}. {t}")

    def eliminar(self, numero):
        # Ajustamos el número ingresado (el usuario pone 1,2,3... pero
        # las listas en Python empiezan en índice 0)
        indice = numero - 1
        # Comprobamos si el índice es válido
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)  # Quitamos la tarea de la lista
        else:
            print("Número inválido.")  # Si no existe, avisamos


# --- Ejemplo de uso ---
todo = ToDoList()          # Creamos la lista de tareas
todo.agregar("Estudiar Python")   # Agregamos una tarea
todo.agregar("Hacer ejercicio")   # Otra tarea
todo.mostrar()              # Mostramos todas las tareas
todo.eliminar(1)            # Eliminamos la primera tarea (Estudiar Python)
todo.mostrar()              # Mostramos la lista actualizada
