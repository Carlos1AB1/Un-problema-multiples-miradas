# --- Paradigma Funcional ---
from functools import reduce

# Las tareas son una lista inmutable (nunca se modifica, siempre se devuelve una nueva).
def agregar_tarea(tareas, tarea):
    return tareas + [tarea]

def mostrar_tareas(tareas):
    list(map(lambda t: print(f"{t[0]}. {t[1]}"), enumerate(tareas, 1)))

def eliminar_tarea(tareas, indice):
    return list(filter(lambda x: x[0] != indice, enumerate(tareas)))

# Uso:
tareas = []
tareas = agregar_tarea(tareas, "Meditar")
tareas = agregar_tarea(tareas, "Hacer mercado")
mostrar_tareas(tareas)
tareas = [t for _, t in eliminar_tarea(tareas, 0)]
mostrar_tareas(tareas)