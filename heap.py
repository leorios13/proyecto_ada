# heap.py
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insertar(self, tarea):
        heapq.heappush(self.heap, tarea)

    def extraer_min(self):
        return heapq.heappop(self.heap) if self.heap else None

    def eliminar_tarea(self, tarea_id):
        self.heap = [t for t in self.heap if t.id != tarea_id]
        heapq.heapify(self.heap)

    def mostrar_heap(self):
        return list(self.heap)