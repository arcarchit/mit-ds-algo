class MaxHeap:


    def __init__(self, ll=[]):
        self.ary = ll
        if ll :
            for i in reversed(range(len(self.ary) / 2 + 1)):
                self.max_heapify(i)


    def max_heapify(self, parent):
        left, right = 2 * parent + 1, 2 * parent + 2
        child_index = parent

        if left < len(self.ary) and self.ary[left] > self.ary[child_index]:
            child_index = left
        if right < len(self.ary) and self.ary[right] > self.ary[child_index]:
            child_index = right

        if child_index != parent:
            self.ary[child_index], self.ary[parent] = self.ary[parent], self.ary[child_index]
            self.max_heapify(child_index)


    def pop(self):
        if not self.ary:
            raise ("Heap is empty")
        popped = self.ary[0]
        self.ary[0] = self.ary[-1]
        del self.ary[-1]
        self.max_heapify(0)
        return popped


    def push(self, element):
        self.ary.append(element)
        self.increase_key(len(self.ary) - 1)


    def increase_key(self, index):
        parent = (index - 1) / 2
        while parent > -1 and self.ary[parent] < self.ary[index]:
            self.ary[index], self.ary[parent] = self.ary[parent], self.ary[index]
            index = parent
            parent = (index - 1) / 2

    def get_length(self):
        return len(self.ary)

    def peek(self):
        if not self.ary:
            raise ("There are no elements in heap")
        return self.ary[0]


def main():

	ll = [3, 4, 6, 1, 2, 9, 8, 5, 7, 0]
	min_heap = MaxHeap(ll)
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