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

class CircularLinkedList:

    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
            self.head.set_pointer(self.head)
        else:
            initial_node = curr_node = self.head

            while curr_node.get_pointer() != initial_node:
                curr_node = curr_node.get_pointer()

            curr_node.set_pointer(Node(data, initial_node))

    def pop(self):

        if self.head == None:
            return False
        else:
            initial_node = curr_node = self.head

            while  curr_node.get_pointer() != initial_node:
                curr_node = curr_node.get_pointer()

            if curr_node == initial_node:
                self.head = None
            else:
                self.head = self.head.get_pointer()
                curr_node.set_pointer(self.head)
            return True

    def size(self):

        size = 0
        initial_node = curr_node = self.head
        while curr_node.get_pointer() != initial_node:
            size += 1
            curr_node = curr_node.get_pointer()

        return size + 1

    def search(self, data):
        initial_node = curr_node = self.head

        while curr_node.get_pointer() != initial_node:

            if curr_node.get_data() == data:
                return True
            curr_node = curr_node.get_pointer()

        if curr_node.get_data() == data:
                return True

        return False

    def as_list(self):
        initial_node = curr_node = self.head
        linked_list = list()
        while curr_node.get_pointer() != initial_node:
            linked_list.append(curr_node.get_data())
            curr_node = curr_node.get_pointer()

        linked_list.append(curr_node.get_data())

        return linked_list

if __name__ == '__main__':

    linked_list = CircularLinkedList()

    # append
    linked_list.push(4)
    linked_list.push(5)
    linked_list.push(1)
    linked_list.push(6)
    linked_list.pop()
    linked_list.pop()


    print(linked_list.as_list())
    print(linked_list.search(1))
    print(linked_list.search(4))
    print(linked_list.size())