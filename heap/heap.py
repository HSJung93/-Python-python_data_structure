class BinaryHeap(object):
    def __init__(self):
        self.heap = [0]
        self.currentSize = 0

    # for shifting the node up
    def shiftUp(self, index):
        while (index // 2) > 0:
            if self.heap[index] < self.heap[index // 2]:     # (currentSize // 2) is the parent 
                temp = self.heap[index // 2]
                self.heap[index // 2] = self.heap[index]
                self.heap[index] = temp
            index = index // 2

    # to insert a node in the heap
    def insert(self, key):
        self.heap.append(key)
        self.currentSize += 1
        self.shiftUp(self.currentSize)

    # for shifting down a node
    def shiftDown(self, index):
        while(index * 2) <= self.currentSize:
            minimumChild = self.minChild(index)
            if self.heap[index] > self.heap[minimumChild]:
                temp = self.heap[index]
                self.heap[index] = self.heap[minimumChild]
                self.heap[minimumChild] = temp
                # print(f"index: {index}, minimumChild: {minimumChild}, \n heap: {self.heap}")
            index = minimumChild
        
    # for finding the child with minimum value
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
        
    # for deleting a node from the heap and maintaining the heap property
    # 끝 노드를 루트 노드로 가져온 이후에 두 자식 노드 중 작은 노드로 노드를 내리면 힙으로 정렬된다.   
    def delete(self):
        deletedNode = self.heap[1]
        self.heap[1] = self.heap[self.currentSize]
        self.currentSize -= 1
        self.heap.pop()
        self.shiftDown(1)
        return deletedNode
    
    # for building heap
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heap = [0] + alist[:]
        while (i > 0):
            self.shiftDown(i)
            i = i - 1

if __name__=="__main__":                
    bh = BinaryHeap()
    bh.buildHeap([9,5,6,2,3,1,11,7,31])

    print(bh.heap)
    print('Deleted:',bh.delete())
    print('Deleted:',bh.delete())
    print(bh.heap)
    print('Deleted:',bh.delete())
    bh.insert(3)
    print(bh.heap)
    print('Deleted:',bh.delete())
    print(bh.heap)