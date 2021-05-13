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

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append(self, data):

        if self.head == None:
            self.tail = self.head = Node(data)
        else:
            prev_node = self.tail
            self.tail = Node(data)
            prev_node.set_pointer(self.tail)

    def prepend(self, data):

        if self.head == None:
            self.tail = self.head = Node(data)
        else:
            next_node = self.head
            self.head = Node(data, next_node)

    def insert(self, data, index):

        is_insert = False

        if self.head == None:
            self.tail = self.head = Node(data)
        else:
            count = 0
            prev_node = curr_node = self.head

            while(curr_node.get_pointer() != None and not is_insert):
                if count == index:
                    if index == 0:
                        self.prepend(data)
                        is_insert = True
                    else:
                        prev_node.set_pointer(Node(data, curr_node))
                        is_insert = True
                        
                count += 1
                prev_node = curr_node
                curr_node = curr_node.get_pointer()

            if not is_insert:
                self.append(data)

    def remove(self, index):

        if self.head == None:
            return False
        else:
            count = 0
            prev_node = curr_node = self.head

            while  curr_node.get_pointer() != None:
                if index == count:
                    if index == 0:
                        curr_head = self.head
                        self.head = curr_head.get_pointer()
                        # curr_head.set_pointer(None)
                        # curr_head.set_data(None)
                        return True
                    else:
                        prev_node.set_pointer(curr_node.get_pointer())
                        # curr_node.set_pointer(None)
                        # curr_node.set_data(None)
                        return True

                count += 1
                prev_node = curr_node
                curr_node = curr_node.get_pointer()

            prev_node.set_pointer(None)
            return True


    def size(self):

        size = 0
        curr_node = self.head
        while curr_node.get_pointer() != None:
            size += 1
            curr_node = curr_node.get_pointer()

        return size + 1

    def search(self, data):
        curr_node = self.head

        while curr_node.get_pointer() != None:

            if curr_node.get_data() == data:
                return True
            curr_node = curr_node.get_pointer()

        if curr_node.get_data() == data:
                return True

        return False

    def as_list(self):
        curr_node = self.head
        linked_list = list()
        while curr_node.get_pointer() != None:
            linked_list.append(curr_node.get_data())
            curr_node = curr_node.get_pointer()

        linked_list.append(curr_node.get_data())

        return linked_list

if __name__ == '__main__':

    linked_list = LinkedList()

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