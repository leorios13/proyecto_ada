# sistema.py
from task import Task
from heap import MinHeap
from avl import AVLTree

class SistemaTareas:
    def __init__(self):
        self.heap = MinHeap() # Inicializa el heap para tareas
        self.avl = AVLTree() # Inicializa el árbol AVL para tareas
        # Raíz del árbol AVL para almacenar tareas por ID
        self.raiz_avl = None

    def agregar_tarea(self, tarea):
        self.heap.insertar(tarea) # Inserta la tarea en el heap
        # Inserta la tarea en el árbol AVL usando su ID como clave
        self.raiz_avl = self.avl.insert(self.raiz_avl, tarea.id, tarea)

    def eliminar_tarea(self, tarea_id):
        self.heap.eliminar_tarea(tarea_id) # Elimina la tarea del heap
        # Elimina la tarea del árbol AVL usando su ID
        self.raiz_avl = self.avl.eliminar(self.raiz_avl, tarea_id)

    def buscar_tarea(self, tarea_id):
        return self.avl.buscar(self.raiz_avl, tarea_id) # Busca una tarea en el árbol AVL por ID

    def tarea_mas_prioritaria(self):
        return self.heap.extraer_min() # Extrae la tarea con menor prioridad (mínimo) del heap

    def mostrar_heap(self):
        return self.heap.mostrar_heap() # Muestra el contenido del heap como una lista