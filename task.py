# task.py
from datetime import datetime

class Task:
    def __init__(self, id, descripcion, prioridad, fecha_vencimiento):
        self.id = id
        self.descripcion = descripcion
        self.prioridad = prioridad  # "Alta", "Media", "Baja"
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")

    def __lt__(self, other):
        prioridad_valor = {"Alta": 1, "Media": 2, "Baja": 3}
        return prioridad_valor[self.prioridad] < prioridad_valor[other.prioridad]

    def __repr__(self):
        return f"[{self.id}] {self.descripcion} ({self.prioridad}) - Vence: {self.fecha_vencimiento.date()}"