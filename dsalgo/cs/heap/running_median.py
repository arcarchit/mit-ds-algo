from min_heap import MinHeap
from max_heap import MaxHeap


class RunningMedian:

    def __init__(self):
        self.left_max_heap = MaxHeap()
        self.right_min_heap = MinHeap()

    def stream_element(self, a):
        left_len, right_len = self.left_max_heap.get_length(), self.right_min_heap.get_length()

        if left_len == right_len:
            self.left_max_heap.push(a)
            return

        if left_len > right_len:
            peek = self.left_max_heap.peek()
            if a >= peek:
                self.right_min_heap.push(a)
            else:
                popped = self.left_max_heap.pop()
                self.left_max_heap.push(a)
                self.right_min_heap.push(popped)
            return

        if left_len < right_len:
            peek = self.right_min_heap.peek()
            if a <= peek:
                self.left_max_heap.push(a)
            else:
                popped = self.right_min_heap.pop()
                self.right_min_heap.push(a)
                self.left_max_heap.push(popped)
            return

    def get_current_median(self):
        left_len, right_len = self.left_max_heap.get_length(), self.right_min_heap.get_length()

        if left_len == 0 and right_len == 0:
            raise ("No element is streamed")

        if left_len > right_len:
            median = self.left_max_heap.peek()
            return median

        if right_len > left_len:
            median = self.right_min_heap.peek()
            return median

        if left_len == right_len:
            median = (self.left_max_heap.peek() + self.right_min_heap.peek())/2.0
            return median


def main():
    rm = RunningMedian()

    rm.stream_element(3)  # Expect 3
    print rm.get_current_median()

    rm.stream_element(5)  # Expect 4
    print rm.get_current_median()

    rm.stream_element(2)  # Expect 3
    print rm.get_current_median()

    rm.stream_element(4)  # Expect 3.5
    print rm.get_current_median()


if __name__ == "__main__":
    main()