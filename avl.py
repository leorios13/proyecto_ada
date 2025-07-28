# avl.py
class AVLNode:
    def __init__(self, key, task):
        self.key = key
        self.task = task
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    # Altura del nodo
    def height(self, node):
        return node.height if node else 0

    # Factor de equilibrio
    def get_balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    # Rotaciones
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    # Insertar
    def insert(self, root, key, task):
        if not root:
            return AVLNode(key, task)
        elif key < root.key:
            root.left = self.insert(root.left, key, task)
        elif key > root.key:
            root.right = self.insert(root.right, key, task)
        else:
            return root  # IDs duplicados no permitidos

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.get_balance(root)

        # Rebalanceo
        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def buscar(self, root, key):
        if not root:
            return None
        if key == root.key:
            return root.task
        elif key < root.key:
            return self.buscar(root.left, key)
        else:
            return self.buscar(root.right, key)

    def eliminar(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.eliminar(root.left, key)
        elif key > root.key:
            root.right = self.eliminar(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min(root.right)
            root.key = temp.key
            root.task = temp.task
            root.right = self.eliminar(root.right, temp.key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.get_balance(root)

        # Rebalanceo
        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def get_min(self, node):
        while node.left:
            node = node.left
        return node