class Node:

    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_pointer(self, pointer):
        self.pointer = pointer

    def get_pointer(self):
        return self.pointer

    def __str__(self):
        return f'(data: {self.data} & pointer: {self.pointer})'


class Queue:

    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def queue(self, data):
        if self.front == None:
            self.front = self.back = Node(data)
        else:
            new_node = Node(data)
            self.back.set_pointer(new_node)
            self.back = self.back.get_pointer()
        return self

    def dequeue(self):
        if self.front == None:
            return None
        else:
            data = self.front.get_data()
            self.front = self.front.get_pointer()

        return data

    def peek(self):
        return self.top.get_data

    def size(self):

        count = 0
        curr_node = self.front

        while curr_node:
            count += 1
            curr_node = curr_node.get_pointer()

        return count

    def as_list(self):
        curr_node = self.front
        stack_list = list()

        while curr_node.get_pointer() != None:
            stack_list.append(curr_node.get_data())
            curr_node = curr_node.get_pointer()

        stack_list.append(curr_node.get_data())

        return stack_list

    def is_empty(self):

        if self.front:
            return False
        else:
            return True
    
    def __str__(self):
        return f'front: {self.front} & back: {self.back}'


if __name__ == '__main__':

    queue = Queue()

    queue.queue('Google')
    queue.queue('Facebook')
    print(queue.queue('Udemy'))
    print(queue.dequeue())

