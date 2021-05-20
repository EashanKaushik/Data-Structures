class MaxHeap:

    def __init__(self):
        self.arr = []
        self.size = 0

    def add_element(self, value):

        if self.size == 0:
            self.arr.append(value)
            self.size += 1
        else:
            # insert
            self.arr.append(value)
            self.size += 1
            current_index = self.size - 1

            # adjust if required
            while current_index > 0:
                parent_index = (current_index - 1) // 2

                if self.arr[parent_index] > self.arr[current_index]:
                    break

                self.arr[parent_index], self.arr[current_index] = self.arr[current_index], self.arr[parent_index]

                current_index = parent_index

    def remove_element(self):

        self.arr[0], self.arr[self.size - 1] = self.arr[self.size - 1], self.arr[0]

        self.arr.pop()
        self.size -= 1

        current_index = 0

        while current_index < self.size - 1:
            left_child = (2 * current_index) + 1
            right_child = (2 * current_index) + 2

            if right_child < self.size:

                if self.arr[left_child] > self.arr[right_child]:
                    self.arr[left_child], self.arr[current_index] = self.arr[current_index], self.arr[left_child]
                    current_index = left_child
                else:
                    self.arr[right_child], self.arr[current_index] = self.arr[current_index], self.arr[right_child]
                    current_index = right_child
            else:
                self.arr[left_child], self.arr[current_index] = self.arr[current_index], self.arr[left_child]
                current_index = left_child

    def return_heap(self):
        return self.arr

    def return_max(self):
        return self.arr[0]

    def return_size(self):
        return self.size


if __name__ == '__main__':
    heap = MaxHeap()

    heap.add_element(2)
    heap.add_element(4)
    heap.add_element(6)
    heap.add_element(5)
    heap.add_element(7)
    heap.add_element(8)
    heap.add_element(10)
    heap.add_element(3)
    # heap.add_element(1)

    print(heap.return_heap())
    print(heap.return_size())
    heap.remove_element()
    heap.remove_element()
    print(heap.return_heap())
