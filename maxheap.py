# MaxHeap
# Public methods: insert, peak, pop
# private methods: __swap, __floatUp, __bubbleDown


class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [None]
        for i in range(len(items)):
            self.heap.append(items[i])
            self.__floatUp(len(self.heap) - 1)

    def __str__(self):
        return str(self.heap)
   
    def insert(self, value):
        self.heap.append(value)
        self.__floatUp(len(self.heap)-1)

    def peak(self):
        if len(self.heap) == 1:
            return False
        return self.heap[1]

    def pop(self):
        self.__swap(1, len(self.heap)-1)
        max_val = self.heap.pop()
        self.__bubbleDown(1)
        return max_val

    def __floatUp(self,i):
        if i == 1:
            return
        else:
            p = i // 2
            if self.heap[i] > self.heap[p]:
                self.__swap(i,p)
                # floating item is now p
                self.__floatUp(p)
    
    def __swap(self,a,b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def __bubbleDown(self, i):
        l = i * 2
        r = (i * 2) + 1
        largest = i
        
        if len(self.heap) > l and self.heap[largest] < self.heap[l]:
            largest = l
        if len(self.heap) > r and self.heap[largest] < self.heap[r]:
            largest = r

        if largest != i:
            self.__swap(i,largest)
            self.__bubbleDown(largest) # not actually the largest at this point

