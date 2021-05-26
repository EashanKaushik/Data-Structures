from node import make_tree

def inorder(root, value):
    stack = list()
    curr_node = root

    while len(stack) > 0 or curr_node:

        if curr_node:
            stack.append(curr_node)
            curr_node = curr_node.left
        else:
            curr_node = stack.pop()

            if curr_node.data == value:
                return True

            curr_node = curr_node.right

def preorder(root, value):
    stack = list()
    curr_node = root

    while len(stack) > 0 or curr_node:

        if curr_node:
            stack.append(curr_node)

            if curr_node.data == value:
                return True

            curr_node = curr_node.left
        else:
            curr_node = stack.pop()
            curr_node = curr_node.right

def postorder(root, value):
    stack = list()
    reverse_stack = list()
    curr_node = root

    while len(stack) > 0 or curr_node:

        if curr_node:
            stack.append(curr_node)
            reverse_stack.append(curr_node.data)
            curr_node = curr_node.right
        else:
            curr_node = stack.pop()
            curr_node = curr_node.left

    while len(reverse_stack) > 0:
        if reverse_stack.pop() == value:
            return True

if __name__ == '__main__':

    root = make_tree()

    print(postorder(root, 5))
