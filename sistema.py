# sistema.py
from task import Task
from heap import MinHeap
from avl import AVLTree

class SistemaTareas:
    def __init__(self):
        self.heap = MinHeap()
        self.avl = AVLTree()
        self.raiz_avl = None

    def agregar_tarea(self, tarea):
        self.heap.insertar(tarea)
        self.raiz_avl = self.avl.insert(self.raiz_avl, tarea.id, tarea)

    def eliminar_tarea(self, tarea_id):
        self.heap.eliminar_tarea(tarea_id)
        self.raiz_avl = self.avl.eliminar(self.raiz_avl, tarea_id)

    def buscar_tarea(self, tarea_id):
        return self.avl.buscar(self.raiz_avl, tarea_id)

    def tarea_mas_prioritaria(self):
        return self.heap.extraer_min()

    def mostrar_heap(self):
        return self.heap.mostrar_heap()