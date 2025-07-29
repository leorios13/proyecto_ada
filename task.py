# task.py
from datetime import datetime

class Task:
    def __init__(self, id, descripcion, prioridad, fecha_vencimiento):
        self.id = id  # ID único de la tarea
        self.descripcion = descripcion # Descripción de la tarea
        self.prioridad = prioridad  # "Alta", "Media", "Baja"
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d") # Fecha de vencimiento en formato YYYY-MM-DD

    def __lt__(self, other):
        # Convierte la prioridad en un valor numérico para comparación
        prioridad_valor = {"Alta": 1, "Media": 2, "Baja": 3}
        prioridad_self = prioridad_valor[self.prioridad]
        prioridad_other = prioridad_valor[other.prioridad]

        # Primero se compara por prioridad
        if prioridad_self != prioridad_other:
            return prioridad_self < prioridad_other
        # Si tienen la misma prioridad, se compara por fecha de vencimiento
        return self.fecha_vencimiento < other.fecha_vencimiento

    def __repr__(self):
        return f"[{self.id}] {self.descripcion} ({self.prioridad}) - Vence: {self.fecha_vencimiento.date()}" # Representación de la tarea para imprimir