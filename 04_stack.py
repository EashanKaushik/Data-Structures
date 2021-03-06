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


class Stack:

    def __init__(self, buttom=None, top=None):
        self.buttom = buttom
        self.top = top

    def push(self, data):
        
        if self.buttom == None:
            self.buttom = self.top = Node(data)
        else:
            new_node = Node(data, self.top)
            self.top = new_node
        return self

    def pop(self):
        
        if self.top == None:
            return None

        self.top = self.top.get_pointer()

    def peek(self):
        return self.top.get_data()

    def as_list(self):

        curr_node = self.top
        stack_list = list()

        while curr_node.get_pointer() != None:
            stack_list.append(curr_node.get_data())
            curr_node = curr_node.get_pointer()

        stack_list.append(curr_node.get_data())

        return stack_list

    def __str__(self):
        return f'top: {self.top} & buttom: {self.buttom}'


if __name__ == '__main__':

    stack = Stack()

    stack.push('Google')
    stack.push('Udemy')
    stack.push('Facebook')
    # print(stack.peek())
    stack.pop()
    print(stack.peek())
    print(stack.as_list())