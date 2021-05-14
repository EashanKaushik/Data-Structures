class Node:

    def __init__(self, data=None, next_pointer=None, prev_pointer = None):
        self.data = data
        self.next_pointer = next_pointer
        self.prev_pointer = prev_pointer

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next_pointer(self, next_pointer):
        self.next_pointer = next_pointer

    def get_next_pointer(self):
        return self.next_pointer

    def set_prev_pointer(self, prev_pointer):
        self.prev_pointer = prev_pointer

    def get_prev_pointer(self):
        return self.prev_pointer


class DoublyLinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append(self, data):

        if self.head == None:
            self.tail = self.head = Node(data)
        else:
            prev_node = self.tail
            self.tail = Node(data, None, prev_node)
            prev_node.set_next_pointer(self.tail)

    def prepend(self, data):

        if self.head == None:
            self.tail = self.head = Node(data)
        else:
            next_node = self.head
            self.head = Node(data, next_node, None)
            next_node.set_prev_pointer(self.head)

    def insert(self, data, index):

        is_insert = False

        if self.head == None:
            self.tail = self.head = Node(data)
        else:
            count = 0
            curr_node = self.head

            while(curr_node.get_next_pointer() != None and not is_insert):
                if count == index:
                    if index == 0:
                        self.prepend(data)
                        is_insert = True
                    else:
                        prev_node = curr_node.get_prev_pointer()
                        prev_node.set_next_pointer(Node(data, curr_node, prev_node))
                        curr_node.set_prev_pointer(prev_node.get_next_pointer())
                        is_insert = True
                        
                count += 1
                curr_node = curr_node.get_next_pointer()

            if not is_insert:
                self.append(data)

    def remove(self, index):

        if self.head == None:
            return False
        else:
            count = 0
            curr_node = self.head

            while  curr_node.get_next_pointer() != None:
                if index == count:
                    if index == 0:
                        curr_head = self.head
                        self.head = curr_head.get_next_pointer()
                        self.head.set_prev_pointer(None)

                        # curr_head.set_next_pointer(None)
                        # curr_head.set_data(None)
                        # curr_head.set_prev_pointer(None)
                        return True
                    else:
                        prev_node = curr_node.get_prev_pointer()
                        prev_node.set_next_pointer(curr_node.get_next_pointer())
                        next_node = prev_node.get_next_pointer()
                        next_node.set_prev_pointer(prev_node)
                        # curr_node.set_pointer(None)
                        # curr_node.set_data(None)
                        return True

                count += 1
                curr_node = curr_node.get_next_pointer()

            prev_node = self.tail.get_prev_pointer()
            prev_node.set_next_pointer(None)
            curr_node.set_prev_pointer(None)
            self.tail = prev_node
            # curr_node.set_data(None)
            return True


    def size(self):

        size = 0
        curr_node = self.head
        while curr_node.get_next_pointer() != None:
            size += 1
            curr_node = curr_node.get_next_pointer()

        return size + 1

    def search(self, data):
        curr_node = self.head

        while curr_node.get_next_pointer() != None:

            if curr_node.get_data() == data:
                return True
            curr_node = curr_node.get_next_pointer()

        if curr_node.get_data() == data:
                return True

        return False

    def as_list(self):
        curr_node = self.head
        linked_list = list()
        while curr_node.get_next_pointer() != None:
            linked_list.append(curr_node.get_data())
            curr_node = curr_node.get_next_pointer()

        linked_list.append(curr_node.get_data())

        return linked_list

    def reverse(self):

        curr_node = self.tail
        linked_list = list()

        while curr_node.get_prev_pointer() != None:
            linked_list.append(curr_node.get_data())
            curr_node = curr_node.get_prev_pointer()

        linked_list.append(curr_node.get_data())

        return linked_list
if __name__ == '__main__':

    linked_list = DoublyLinkedList()

    # append
    linked_list.append(4)
    linked_list.append(2)
    linked_list.append(1)
    linked_list.append(100)
    linked_list.append(50)
    linked_list.append(0)

    # prepend
    linked_list.prepend(1)
    linked_list.prepend(50)
    linked_list.prepend(2)
    linked_list.append(100)
    linked_list.append(50)
    linked_list.append(0)
    linked_list.prepend(99)
    linked_list.append(999)

    # insert
    linked_list.insert(8, 0)
    linked_list.insert(5, 1)
    linked_list.insert(1, 2)
    linked_list.insert(2, 1)
    linked_list.insert(4, 3)
    linked_list.prepend(99)
    linked_list.append(100)


    print(linked_list.as_list())
    print(linked_list.search(1000))
    print(linked_list.remove(1000))
    print(linked_list.as_list())
    print(linked_list.search(1000))
    print(linked_list.remove(50))
    print(linked_list.search(50))
    print(linked_list.as_list())
    print(linked_list.as_list())
    print(linked_list.size())
    print(linked_list.reverse())