# avl.py
class AVLNode:
    def __init__(self, key, task):
        self.key = key  
        self.task = task   # Objeto tarea que contiene ID, prioridad y fecha de vencimiento
        self.height = 1    # Altura del nodo (inicialmente 1 al crearse el nodo hoja)
        self.left = None   # Hijo izquierdo
        self.right = None  # Hijo derecho

class AVLTree:
    """
    Árbol AVL para almacenar tareas por su ID de manera balanceada.
    """
    def __init__(self):
        self.root = None # Raíz inicial del árbol

    # Altura del nodo
    def height(self, node):
        """
        Devuelve la altura de un nodo.
        """
        return node.height if node else 0

    # Factor de equilibrio
    def get_balance(self, node):
        """
        Calcula el factor de balance de un nodo (altura izquierda - altura derecha).
        """
        return self.height(node.left) - self.height(node.right) if node else 0

    # Rotaciones
    def right_rotate(self, y):
        """
        Rotación simple a la derecha para balancear desbalance hacia la izquierda.
        """
        x = y.left 
        T2 = x.right 
        x.right = y 
        y.left = T2 
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def left_rotate(self, x):
        """
        Rotación simple a la izquierda para balancear desbalance hacia la derecha.
        """
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    # Insertar
    def insert(self, root, key, task):
        """
        Inserta una tarea en el árbol AVL y aplica rotaciones si es necesario para mantener el balance.
        """
        if not root:
            return AVLNode(key, task)  # Caso base: insertar en hoja
        
        # Inserción recursiva a izquierda o derecha
        elif key < root.key:
            root.left = self.insert(root.left, key, task)
        elif key > root.key:
            root.right = self.insert(root.right, key, task)
        else:
            return root  # IDs duplicados no permitidos
        
        # Actualizar altura del nodo actual
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        # Calcular el balance del nodo actual
        balance = self.get_balance(root)

        # Rebalanceo: Rotaciones necesarias según el caso de desbalance
        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root) # Caso LL
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root) # Caso LR
        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root) # Caso RR
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root) # Caso RL
        return root

    def buscar(self, root, key):
        """
        Busca una tarea por ID de manera recursiva.
        """
        if not root:
            return None # Si el nodo es None, la tarea no existe
        if key == root.key:
            return root.task # Si el ID coincide, retornar la tarea
        elif key < root.key:
            return self.buscar(root.left, key) # Buscar en subárbol izquierdo
        else:
            return self.buscar(root.right, key) # Buscar en subárbol derecho

    def eliminar(self, root, key):
        """
        Elimina una tarea por ID del árbol AVL y rebalancea si es necesario.
        """
        if not root:
            return root # Si el nodo es None, no hay nada que eliminar
        
        # Recorrido recursivo para encontrar el nodo a eliminar
        elif key < root.key:
            root.left = self.eliminar(root.left, key) # Buscar en subárbol izquierdo
        elif key > root.key:
            root.right = self.eliminar(root.right, key) # Buscar en subárbol derecho
        else:
            if not root.left:
                return root.right # Si no hay hijo izquierdo, retornar hijo derecho
            elif not root.right:
                return root.left # Si no hay hijo derecho, retornar hijo izquierdo
            # Nodo con dos hijos: encontrar el sucesor inorden (mínimo en el sub árbol derecho)
            temp = self.get_min(root.right)
            root.key = temp.key # Reemplazar clave del nodo a eliminar con el sucesor
            root.task = temp.task # Reemplazar tarea del nodo a eliminar con la del sucesor
            root.right = self.eliminar(root.right, temp.key) # Eliminar el sucesor inorden

        # Actualizar altura del nodo actual después de la eliminación
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.get_balance(root)

        # Rebalanceo tras eliminación
        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root) # Caso LL
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root) # Caso LR
        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)   # Caso RR
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root) # Caso RL
        return root 

    def get_min(self, node):
        """
        Devuelve el nodo con el valor mínimo (más a la izquierda).
        """
        while node.left: 
            node = node.left 
        return node 