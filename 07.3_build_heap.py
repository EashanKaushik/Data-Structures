class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(self.arr)

    def max_heapify(self, current_index):

        if not self.is_leaf(current_index):
            left_child = (2 * current_index) + 1
            right_child = (2 * current_index) + 2

            if right_child < self.size:

                if self.arr[left_child] > self.arr[current_index] or self.arr[right_child] > self.arr[current_index]:

                    if self.arr[left_child] > self.arr[right_child]:
                        self.arr[left_child], self.arr[current_index] = self.arr[current_index], self.arr[left_child]
                        self.max_heapify(left_child)
                    else:
                        self.arr[right_child], self.arr[current_index] = self.arr[current_index], self.arr[right_child]
                        self.max_heapify(right_child)
            else:
                if self.arr[left_child] > self.arr[current_index]:
                    self.arr[left_child], self.arr[current_index] = self.arr[current_index], self.arr[left_child]
                    self.max_heapify(left_child)

    def build_heap(self):

        for index in range((self.size//2) - 1, -1, -1):
            self.max_heapify(index)

    def is_leaf(self, current_index):

        if current_index >= self.size // 2 and current_index <= self.size - 1:
            return True

        return False

    def return_arr(self):
        return self.arr

if __name__ == '__main__':

    heap = Heap([3, 6, 5, 0, 8, 2, 1, 9])
    heap.build_heap()
    print(heap.return_arr())
