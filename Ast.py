
class treeNode:
    def __init__(self, value, child=None, brother=None):
        self.value = value
        self.child = child
        self.brother = brother

class AST:
    def __init__(self):
        self.root = None
        self.current = None

    def makeNode(self, value, child, brother):
        node = treeNode(value=value, child=child, brother=brother)
        if self.root is None:
            self.root = node
            self.current = node
        return node

    def makeLeaf(self, value):
        node = treeNode(value=value, child=None, brother=None)
        if self.root is None:
            self.root = node
            self.current = node
        return node

    def addChild(self, father, new_child):
        if father.child is None:
            father.child = new_child
            self.current = new_child
            return

        node = father.child
        while node.brother is not None:
            node = node.brother
        node.brother = new_child
        self.current = new_child

    def addBrother(self, node, new_brother):
        if node is None:
            return

        while node.brother is not None:
            node = node.brother
        node.brother = new_brother
        self.current = new_brother
