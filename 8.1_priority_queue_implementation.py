from classes.node import Node

class PriorityQueue:

    def __init__(self, root=None):
        self.arr = []
        self.size = 0

    def add(self, value):

        self.arr.append(value)
        self.size += 1
        current_index = self.size - 1

        while current_index > 0:
            parent_index = (current_index - 1) // 2

            if self.arr[parent_index] < self.arr[current_index]:
                break

            self.arr[parent_index], self.arr[current_index] = self.arr[current_index], self.arr[parent_index]
            current_index = parent_index

    def poll(self):

        if self.size == 0:
            return

        self.arr[0], self.arr[self.size - 1] = self.arr[self.size - 1], self.arr[0]
        value = self.arr.pop()
        self.size -= 1

        if self.size > 0:
            self.heapify(0)

        print(value)

    def heapify(self, current_index):

        if not self.is_leaf(current_index):
            left_child = 2 * current_index + 1
            right_child = 2 * current_index + 2

            if right_child < self.size:
                if self.arr[right_child] < self.arr[current_index] or self.arr[left_child] < self.arr[current_index]:
                    if self.arr[right_child] < self.arr[left_child]:
                        self.arr[right_child], self.arr[current_index] = self.arr[current_index], self.arr[right_child]
                        self.heapify(right_child)
                    else:
                        self.arr[left_child], self.arr[current_index] = self.arr[current_index], self.arr[left_child]
                        self.heapify(left_child)
            else:
                if self.arr[left_child] < self.arr[current_index]:
                    self.arr[left_child], self.arr[current_index] = self.arr[current_index], self.arr[left_child]
                    self.heapify(left_child)

    def is_leaf(self, current_index):

        if current_index >= self.size // 2 and current_index <= self.size - 1:
            return True

        return False

    def contains(self, value):
        if self.size == 0:
            return
        else:
            if value in self.arr:
                return True

            return False

    def poll_rest(self):

        while self.size > 0:
            self.poll()

    def peek(self):
        return self.arr[0]

    def __str__(self):
        return f'Heap: {self.arr} & size {self.size}'


if __name__ == '__main__':
    heapq = PriorityQueue()

    heapq.add(5)
    heapq.add(2)
    heapq.poll()
    print(heapq)
    heapq.add(1)
    heapq.poll()
    print(heapq)
    heapq.add(4)
    heapq.add(10)
    heapq.add(11)
    print(heapq)
    heapq.poll_rest()

    print('Second')
    heapq.add(5)
    heapq.add(12)
    heapq.add(8)
    heapq.poll()
    heapq.add(17)
    heapq.add(3)
    heapq.poll()
    heapq.add(7)
    heapq.add(23)
    heapq.poll()
    heapq.add(46)
    heapq.add(69)
    heapq.poll()
    heapq.poll()
    heapq.poll()
    heapq.add(1)
    heapq.poll_rest()
