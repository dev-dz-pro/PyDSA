class MinHeap:
    def __init__(self):
        self.binary_heap = [None]

    def insert(self, node):
        self.binary_heap.append(node)
        parent = int((len(self.binary_heap)-1) / 2)
        current = len(self.binary_heap) - 1
        while parent > 0:
            if self.binary_heap[current] < self.binary_heap[parent]:
                self.binary_heap[current], self.binary_heap[parent] = self.binary_heap[parent], self.binary_heap[current]
                current = parent
                parent = int(current / 2)
            else:
                break
            
    def extract_min(self):
        return self.binary_heap[1]

    def delete_min(self):
        x = self.binary_heap.pop()
        self.binary_heap[1] = x
        current = 1
        length = len(self.binary_heap) 
        while (current*2 < length and self.binary_heap[current * 2] < self.binary_heap[current]) or (current*2+1 < length and self.binary_heap[current * 2 + 1] < self.binary_heap[current]):
            if self.binary_heap[current * 2] < self.binary_heap[current * 2 + 1]:
                self.binary_heap[current], self.binary_heap[current * 2] = self.binary_heap[current * 2], self.binary_heap[current]
                current = current * 2
            else:
                self.binary_heap[current], self.binary_heap[current * 2 + 1] = self.binary_heap[current * 2 + 1], self.binary_heap[current]
                current = current * 2 + 1


    def get_tree(self):
        return [x for i, x in enumerate(self.binary_heap) if i > 0]


if __name__ == '__main__':
    heap = MinHeap()
    heap.insert(10)
    heap.insert(45)
    heap.insert(5)
    heap.insert(12)
    heap.insert(9)
    heap.insert(2)
    print("-------------------GETMIN before deletion-------------------")
    print(heap.extract_min())
    print("-------------------GETTREE before deletion-------------------")
    print(heap.get_tree())
    print("-------------------DELETE-------------------")
    heap.delete_min()
    print("-------------------GETMIN after deletion-------------------")
    print(heap.extract_min())
    print("-------------------GETTREE after deletion-------------------")
    print(heap.get_tree())