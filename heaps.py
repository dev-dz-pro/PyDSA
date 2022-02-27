class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class MinHeap:
    def __init__(self):
        self.tree = [None]

    def insert(self, node):
        self.tree.append(node)
        parent = int((len(self.tree)-1) / 2)
        current = len(self.tree) - 1
        while parent > 0:
            if self.tree[current].data < self.tree[parent].data:
                self.tree[current], self.tree[parent] = self.tree[parent], self.tree[current]
                current = parent
                parent = int(current / 2)
            else:
                break
            

    def extract_min(self):
        return self.tree[1].data


    def print_tree(self):
        pass


    def search(self, data):
        pass


    def delete(self, data):
        pass


if __name__ == '__main__':
    heap = MinHeap()
    heap.insert(Node(10))
    heap.insert(Node(45))
    heap.insert(Node(5))
    heap.insert(Node(12))
    heap.insert(Node(4))
    heap.insert(Node(9))
    heap.insert(Node(2))
    print(heap.extract_min())