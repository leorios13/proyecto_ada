import tkinter as tk
from tkinter import messagebox, ttk
from sistema import SistemaTareas
from task import Task

class App:
    def __init__(self, root):
        self.sistema = SistemaTareas()
        self.root = root
        self.root.title("Gestión de Tareas - AVL + Heap")

        # Entrada de datos
        self.frame_entrada = tk.Frame(root)
        self.frame_entrada.pack(pady=10)

        tk.Label(self.frame_entrada, text="ID:").grid(row=0, column=0)
        self.entry_id = tk.Entry(self.frame_entrada)
        self.entry_id.grid(row=0, column=1)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=1, column=0)
        self.entry_desc = tk.Entry(self.frame_entrada)
        self.entry_desc.grid(row=1, column=1)

        tk.Label(self.frame_entrada, text="Prioridad:").grid(row=2, column=0)
        self.combo_prioridad = ttk.Combobox(self.frame_entrada, values=["Alta", "Media", "Baja"])
        self.combo_prioridad.grid(row=2, column=1)

        tk.Label(self.frame_entrada, text="Vencimiento (YYYY-MM-DD):").grid(row=3, column=0)
        self.entry_fecha = tk.Entry(self.frame_entrada)
        self.entry_fecha.grid(row=3, column=1)

        tk.Button(self.frame_entrada, text="Agregar tarea", command=self.agregar).grid(row=4, column=0, columnspan=2, pady=5)

        # Botones de acción
        self.frame_acciones = tk.Frame(root)
        self.frame_acciones.pack(pady=10)
        
        tk.Button(self.frame_acciones, text="Mostrar Heap", command=self.mostrar_heap).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_acciones, text="Tarea más prioritaria", command=self.extraer_prioritaria).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_acciones, text="Buscar tarea por ID", command=self.buscar_tarea).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_acciones, text="Eliminar tarea por ID", command=self.eliminar_tarea).pack(side=tk.LEFT, padx=5)

        # Área de resultados
        self.text_resultado = tk.Text(root, height=10, width=70)
        self.text_resultado.pack(pady=10)

    def agregar(self):
        try:
            id = int(self.entry_id.get())
            desc = self.entry_desc.get()
            prioridad = self.combo_prioridad.get()
            fecha = self.entry_fecha.get()
            tarea = Task(id, desc, prioridad, fecha)
            self.sistema.agregar_tarea(tarea)
            messagebox.showinfo("Éxito", f"Tarea agregada: {desc}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mostrar_heap(self):
        tareas = self.sistema.mostrar_heap()
        self.text_resultado.delete(1.0, tk.END)
        for t in tareas:
            self.text_resultado.insert(tk.END, str(t) + "\n")

    def extraer_prioritaria(self):
        tarea = self.sistema.tarea_mas_prioritaria()
        if tarea:
            respuesta = messagebox.askquestion("Tarea prioritaria", f"{tarea}\n\n¿Ha completado la tarea?")
            if respuesta == 'yes':
                self.sistema.eliminar_tarea(tarea.id)
                messagebox.showinfo("Tarea completada", "¡Tarea completada!")
            else:
                self.sistema.agregar_tarea(tarea)
            
        else:
            messagebox.showinfo("Info", "No hay tareas disponibles")

    def buscar_tarea(self):
        try:
            id = int(self.entry_id.get())
            tarea = self.sistema.buscar_tarea(id)
            self.text_resultado.delete(1.0, tk.END)
            if tarea:
                self.text_resultado.insert(tk.END, f"Tarea encontrada: {tarea}\n")
            else:
                self.text_resultado.insert(tk.END, "Tarea no encontrada\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_tarea(self):
        try:
            id = int(self.entry_id.get())
            self.sistema.eliminar_tarea(id)
            messagebox.showinfo("Éxito", f"Tarea con ID {id} eliminada")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
