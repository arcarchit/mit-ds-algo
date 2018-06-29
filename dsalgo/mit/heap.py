# heap property : Both children should be left than parents, there is nothing like left or right
# heapify moves node toward leaves swapping with its children while Increase - Decrease key - travels towards root
# In max heap increase key is somewhat complicated, travels towards root, while decrease key is simply heapify
# Insert is done with increase/decrease key

# Min - Heapify property has <=, equal is there

class Node:

    def __init__(self, name, key):
        self.name = name
        self.key = key

    def __lt__(self, other):
        return self.key < other.key


# We are implementing min heap here, we want to use it in dijkstras
class PQ:

    def __init__(self):
        self.hp = []

    def build_min_heap(self, ll):
        self.hp = ll
        for i in range(len(ll)/2 + 1, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        # 0, 1, 2, 3, 4, 5, 6, 7
        # left = 2*i + 1, right = 2*i + 2
        left, right = 2*i + 1, 2*i + 2
        smallest = i

        if left < len(self.hp)  and self.hp[i] > self.hp[left]:
            smallest = left

        if right < len(self.hp)  and self.hp[smallest] > self.hp[right]:
            smallest = right

        if smallest != i:
            self.hp[i], self.hp[smallest] = self.hp[smallest], self.hp[i]
            self.min_heapify(smallest)

    def insert(self, new_val):
        self.hp.append(new_val)
        self.decrease_key(len(self.hp)-1, new_val)

    def min(self):
        return self.hp[0]

    def decrease_key(self, i, new_val):
        current_val = self.hp[i]
        if new_val > current_val:
            raise Exception("New value is larger than current value")
        self.hp[i] = new_val
        while i != 0:
            # 0, 1, 2, 3, 4, 5
            # parent = (i - 1)/2
            parent = (i - 1)/2
            if self.hp[parent] > self.hp[i]:
                self.hp[parent], self.hp[i] = self.hp[i], self.hp[parent]
                i = parent
            else:
                break

    def extract_min(self):
        val = self.hp[0]
        last = self.hp.pop(-1)
        self.hp[0] = last
        self.min_heapify(0)
        return val



def main():
    pq = PQ()
    ll = [5,2,6,8,0,1,2,4]
    pq.build_min_heap(ll)
    print pq.hp   # Should return  [0, 2, 1, 4, 5, 6, 2, 8]
    pq.decrease_key(3,1)
    print pq.hp   # Should return [0, 1, 1, 2, 5, 6, 2, 8
    pq.extract_min()
    print pq.hp    # Should return [1, 2, 1, 8, 5, 6, 2]
    print pq.min()
    pq.insert(9)
    print "after inserting 9 ", pq.hp
    pq.insert(0)
    print "after inserting 0 ", pq.hp


if __name__ == "__main__":
    main()