class MinHeap:


    def __init__(self, ll=[]):
		# Complexity of buildHeap : O(N log N)
        self.ary = ll
        if ll :
            for i in reversed(range(len(self.ary) / 2 + 1)):
                self.min_heapify(i)


    def min_heapify(self, parent):
		# Complexity : O(log N)
        left, right = 2 * parent + 1, 2 * parent + 2

        child_index = parent

        if left < len(self.ary) and self.ary[left] < self.ary[child_index]:
            child_index = left
        if right < len(self.ary) and self.ary[right] < self.ary[child_index]: # IT IS A SMALLEST CHILD INDEX, ELSE AFTER SWAP HEAP PROPERTY WONT HOLD
            child_index = right

        if child_index != parent:
            self.ary[child_index], self.ary[parent] = self.ary[parent], self.ary[child_index]
            self.min_heapify(child_index)


    def push(self, a):
		# Complexity : O(log N)
        self.ary.append(a)
        self.decrease_key(len(self.ary) - 1)


    def decrease_key(self, index):
		# Complexity : O(log N)
        parent = (index - 1) / 2
        while parent > -1 and self.ary[parent] > self.ary[index]:
            self.ary[index], self.ary[parent] = self.ary[parent], self.ary[index]
            index = parent
            parent = (index - 1) / 2


    def pop(self):
		# Complexity : O(log N)
        if not self.ary:
            raise ("There are no elements in heap")
        popped = self.ary[0]
        self.ary[0] = self.ary[-1]
        del self.ary[-1]
        self.min_heapify(0)
        return popped

    def get_length(self):
        return len(self.ary)

    def peek(self):
        if not self.ary:
            raise ("There are no elements in heap")
        return self.ary[0]


def main():

	ll = [3, 4, 6, 1, 2, 9, 8, 5, 7, 0]
	min_heap = MinHeap(ll)
	print min_heap.ary
	for _ in range(2):
		print min_heap.pop()
	min_heap.push(11)
	min_heap.push(0)
	print min_heap.ary
	for _ in range(2):
		print min_heap.pop()


if __name__=="__main__":
    main()

