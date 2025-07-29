# heap.py
import heapq

class MinHeap:
    def __init__(self):
        self.heap = [] # Inicializa el heap vacío

    def insertar(self, tarea):
        heapq.heappush(self.heap, tarea) # Inserta una tarea en el heap

    def extraer_min(self):
        return heapq.heappop(self.heap) if self.heap else None # Extrae la tarea con menor prioridad (mínimo)

    def eliminar_tarea(self, tarea_id):
        self.heap = [t for t in self.heap if t.id != tarea_id] # Elimina una tarea por ID
        heapq.heapify(self.heap) # Reorganiza el heap después de eliminar una tarea

    def mostrar_heap(self):
        return list(self.heap) # Muestra el contenido del heap como una lista