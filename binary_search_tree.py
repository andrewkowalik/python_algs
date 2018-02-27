
class Tree(object):
    def __init__(self, value=None):
        if value:
            self.root = Node(value)

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)
            return True

    def find(self, value):
        if self.root:
            return self.root.find(value)
        else:
            return False

    def preorder(self):
        return self.root.preorder()

    def postorder(self):
        return self.root.postorder()

    def inorder(self):
        return self.root.inorder()


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert(self, value):
        if value == self.value:
            return False
        elif value < self.value:
            try:
                return self.left_child.insert(value)
            except AttributeError:
                self.left_child = Node(value)
                return True
        elif value > self.value:
            try:
                return self.right_child.insert(value)
            except AttributeError:
                self.right_child = Node(value)
                return True

    def find(self, value):
        if self.value == value:
            return True
        elif value < self.value:
            try:
                return self.left_child.find(value)
            except AttributeError:
                return False
        elif value > self.value:
            try:
                return self.right_child.find(value)
            except AttributeError:
                return False

        return False

    def preorder(self, values=None):
        if not values:
            values = []

        values.append(self.value)
        if self.left_child:
            self.left_child.preorder(values)
        if self.right_child:
            self.right_child.preorder(values)
        return values

    def postorder(self, values=None):
        if not values:
            values = []

        if self.left_child:
            self.left_child.preorder(values)
        if self.right_child:
            self.right_child.preorder(values)
        values.append(self.value)
        return values

    def inorder(self, values=None):
        if not values:
            values = []

        if self.left_child:
            self.left_child.preorder(values)
        values.append(self.value)
        if self.right_child:
            self.right_child.preorder(values)

        return values
