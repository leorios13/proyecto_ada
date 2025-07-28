# test.py
from sistema import SistemaTareas
from task import Task

sistema = SistemaTareas()

t1 = Task(101, "Estudiar para el examen", "Alta", "2025-07-30")
t2 = Task(102, "Comprar útiles escolares", "Media", "2025-07-25")
t3 = Task(103, "Revisar correos electrónicos", "Baja", "2025-07-24")

sistema.agregar_tarea(t1)
sistema.agregar_tarea(t2)
sistema.agregar_tarea(t3)

print("Heap actual:")
print(sistema.mostrar_heap())

print("\nTarea más prioritaria extraída:")
print(sistema.tarea_mas_prioritaria())

print("\nBuscar tarea ID 102:")
print(sistema.buscar_tarea(102))

print("\nEliminar tarea ID 102:")
sistema.eliminar_tarea(102)
print(sistema.buscar_tarea(102))

print("Heap actual:")
print(sistema.mostrar_heap())