tareas = []

def agregar_tarea(tarea):
    tareas.append(tarea)

def mostrar_tareas():
    for i, t in enumerate(tareas, 1):
        print(f"{i}. {t}")

def eliminar_tarea(indice):
    if 0 <= indice < len(tareas):
        tareas.pop(indice)

# Uso:
agregar_tarea("Estudiar para el examen")
agregar_tarea("Hacer ejercicio")
mostrar_tareas()
eliminar_tarea(0)
mostrar_tareas()
