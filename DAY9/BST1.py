# creating an object means creating a separate node

class Node:
    # create a node in the tree
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        



class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # insert root node if there is no root node
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertnode(self.root, value)

    def insertnode(self, rootnode, value):
        if value < rootnode.data:
            if rootnode.left is None:
                rootnode.left = Node(value)
            else:
                self.insertnode(rootnode.left, value)
        else:
            if rootnode.right is None:
                rootnode.right = Node(value)
            else:
                self.insertnode(rootnode.right, value)

    def searchnode(self, rootnode, value):
        if rootnode is None:
            return "Value not found"

        if rootnode.data == value:
            return "Value found"

        elif value < rootnode.data:
            return self.searchnode(rootnode.left, value)

        else:
            return self.searchnode(rootnode.right, value)

    def inorder(self, rootnode):
        if rootnode is not None:
            self.inorder(rootnode.left)
            print(rootnode.data, end=" ")
            self.inorder(rootnode.right)

    def preorder(self, rootnode):
        if rootnode is not None:
            print(rootnode.data, end=" ")
            self.preorder(rootnode.left)
            self.preorder(rootnode.right)

    def postorder(self, rootnode):
        if rootnode is not None:
            self.postorder(rootnode.left)
            self.postorder(rootnode.right)
            print(rootnode.data, end=" ")

    def deletetree(self):
        self.root = None
        return "Tree deleted successfully"


# object creation
btobj = BinaryTree()
btobj.insert(50)
btobj.insert(30)
btobj.insert(70)
btobj.insert(20)
btobj.insert(40)
btobj.insert(60)
btobj.insert(80)

print("Inorder Traversal:")
btobj.inorder(btobj.root)

print("\nPreorder Traversal:")
btobj.preorder(btobj.root)

print("\nPostorder Traversal:")
btobj.postorder(btobj.root)

print("\nSearch 40:", btobj.searchnode(btobj.root, 40))
print("Search 100:", btobj.searchnode(btobj.root, 100))

print(btobj.deletetree())