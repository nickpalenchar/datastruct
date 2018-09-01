# MaxHeap
# Public methods: insert, peak, pop
# private methods: __swap, __floatUp, __bubbleDown


class MaxHeap:
    def __init__(self, items=[]):
        self.heap = [None]
        for i in range(len(items)):
            self.heap.append(items[i])
            self.__floatUp(len(self.heap) - 1)

    def insert(self):
	pass

    def peak(self):
        pass

    def pop(self):
        pass
