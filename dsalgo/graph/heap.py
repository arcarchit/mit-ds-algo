
class max_heap:

    def __init__(self, ll):
        self.data = ll
        self.len = len(ll)

    def heap_sort(self):
        self.build_heap()
        while self.len > 0:
            last_index = self.len - 1
            self.data[0], self.data[last_index] = self.data[last_index], self.data[0]
            self.len = self.len - 1
            self.max_heapify(0)
        return self.data

    def max_heapify(self, index):
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            left_condition = (left < self.len)
            right_condition = (right < self.len)

            if left_condition and right_condition:
                swap_index = left if self.data[left] > self.data[right] else right
            elif left_condition:
                swap_index = left
            elif right_condition:
                swap_index = right
            else:
                break
            self.data[index], self.data[swap_index] = self.data[swap_index], self.data[index]
            index = swap_index

    def build_heap(self):
        upper = (self.len-1)/2
        for i in range(upper, -1, -1):
            self.max_heapify(i)


ll = [5, 7, 9, 1, 4, 3, 2, 6, 8]
mh = max_heap(ll)
mh.build_heap()
mh.heap_sort()
print mh.data