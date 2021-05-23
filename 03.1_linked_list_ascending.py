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


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def add_node(self, data):

        # empty list
        if self.head == None:
            self.head = Node(data)

        else:
            curr_node = self.head

            if data < curr_node.get_data():
                self.head = Node(data, curr_node)
            else:
                while curr_node.get_data() < data and curr_node.get_pointer() != None:
                    prev_node = curr_node
                    curr_node = curr_node.get_pointer()

                if curr_node.get_data() > data:
                    prev_node.set_pointer(Node(data, curr_node))

                elif curr_node.get_data() < data and curr_node.get_pointer() == None:
                    curr_node.set_pointer(Node(data))

                else:
                    prev_node.set_pointer(Node(data, curr_node))

    def return_list(self):

        curr_node = self.head
        linked_list = list()
        while curr_node.get_pointer() != None:
            linked_list.append(curr_node.get_data())

            curr_node = curr_node.get_pointer()

        linked_list.append(curr_node.get_data())

        return linked_list

    def search(self, data):
        curr_node = self.head

        while curr_node.get_pointer() != None:

            if curr_node.get_data() == data:
                return True
            curr_node = curr_node.get_pointer()

        if curr_node.get_data() == data:
                return True

        return False

    def delete(self, data):
        prev_node = curr_node = self.head

        while curr_node.get_pointer() != None:
            if curr_node.get_data() == data:
                if prev_node == curr_node:
                    self.head = curr_node.get_pointer()
                    # curr_node.set_pointer(None)
                    # curr_node.set_data(None)
                    return True
                else:
                    prev_node.set_pointer(curr_node.get_pointer())
                    # curr_node.set_pointer(None)
                    # curr_node.set_data(None)
                    return True

            prev_node = curr_node
            curr_node = curr_node.get_pointer()


        if curr_node.get_data() == data:
                prev_node.set_pointer(None)
                # curr_node.set_pointer(None)
                # curr_node.set_data(None)
                return True

        return False

    def size(self):
        size = 0
        curr_node = self.head
        while curr_node.get_pointer() != None:

            size += 1
            curr_node = curr_node.get_pointer()

        size += 1
        return size


if __name__ == '__main__':

    linked_list = LinkedList()

    linked_list.add_node(4)
    linked_list.add_node(2)
    linked_list.add_node(1)
    linked_list.add_node(3)
    linked_list.add_node(8)
    linked_list.add_node(10)
    linked_list.add_node(5)
    linked_list.add_node(9)
    linked_list.add_node(5)
    linked_list.add_node(7)
    linked_list.add_node(7)
    linked_list.add_node(6)
    linked_list.add_node(100)
    linked_list.add_node(1000)
    linked_list.add_node(150)
    linked_list.add_node(50)






    print(linked_list.return_list())
    print(linked_list.search(1000))
    print(linked_list.delete(1000))
    print(linked_list.return_list())
    print(linked_list.search(1000))
    print(linked_list.delete(50))
    print(linked_list.search(50))
    print(linked_list.return_list())
    linked_list.add_node(50)
    print(linked_list.return_list())
    print(linked_list.size())


