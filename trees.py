class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self, root) -> None:
        self.root = root


    def insert(self, data, node):
        if data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert(data, node.right)
        elif data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert(data, node.left)
                 
            
    def search(self, data, node):
        if data == node.data:
            return node.data
        elif data > node.data:
            if node.right is None:
                return None
            else:
                return self.search(data, node.right)
        elif data < node.data:
            if node.left is None:
                return None
            else:
                return self.search(data, node.left)


    def inorder(self, node):
        if node.left is not None:
            self.inorder(node.left)
        print(node.data)
        if node.right is not None:
            self.inorder(node.right)

    def preorder(self, node):
        print(node.data)
        if node.left is not None:
            self.preorder(node.left)
        if node.right is not None:
            self.preorder(node.right)

    def postorder(self, node):
        if node.left is not None:
            self.postorder(node.left)
        if node.right is not None:
            self.postorder(node.right)
        print(node.data)

    



if __name__ == '__main__':
    root = Node(1)
    tree = Tree(root)
    tree.insert(4, root)
    tree.insert(3, root)
    tree.insert(6, root)
    tree.insert(2, root)
    tree.insert(5, root)
    print("-------------------search-------------------")
    print(tree.search(9, root))
    print("-------------------inorder------------------")
    tree.inorder(root)
    print("------------------preorder-------------------")
    tree.preorder(root)
    print("------------------postorder-------------------")
    tree.postorder(root)