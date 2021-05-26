from node import make_tree

def diagonal_traversal(root, value):

    queue = list()
    diagonal_node_value = dict()

    queue.append(root)
    queue.append(0)

    while len(queue) > 0:

        curr_node = queue.pop(0)
        curr_val = queue.pop(0)

        if curr_node.left:
            queue.append(curr_node.left)
            queue.append(curr_val + 1)

        if curr_node.right:
            queue.append(curr_node.right)
            queue.append(curr_val)

        if curr_val in diagonal_node_value:
            diagonal_node_value[curr_val].append(curr_node.data)
        else:
            diagonal_node_value[curr_val] = [curr_node.data]

    for value in sorted(diagonal_node_value):
        for node in diagonal_node_value[value]:
            if node == curr_node.data:
                return True

def boundary_traversal(root, value):

    # left side
    curr_node = root

    while 1:
        # print(curr_node.data)
        if curr_node.data == value:
            return True

        if curr_node.left:
            curr_node = curr_node.left
        elif curr_node.right:
            curr_node = curr_node.right
        else:
            break

    # leaf nodes
    queue = list()
    queue.append(root)

    while len(queue) > 0:
        curr_node = queue.pop(0)

        if not curr_node.left and not curr_node.right:
            # print(curr_node.data)
            if curr_node.data == value:
                return True
        else:
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

    # right nodes
    curr_node = root.right
    # stack = list()
    while 1:
        # stack.append(curr_node.data)
        if curr_node.data == value:
            return True

        if curr_node.right:
            curr_node = curr_node.right
        elif curr_node.left:
            curr_node = curr_node.left
        else:
            break

    # while len(stack) > 0:
    #     print(stack.pop())

def spiral_traversal(root, value):

    l_r_stack = list()
    r_l_stack = list()

    l_r_stack.append(root)

    while len(l_r_stack) > 0 or len(r_l_stack) > 0:

        while len(l_r_stack) > 0:
            curr_node = l_r_stack.pop()

            # print(curr_node.data)

            if curr_node.data == value:
                return True

            if curr_node.right:
                r_l_stack.append(curr_node.right)

            if curr_node.left:
                r_l_stack.append(curr_node.left)

        while len(r_l_stack) > 0:

            curr_node = r_l_stack.pop()

            # print(curr_node.data)

            if curr_node.data == value:
                return True

            if curr_node.left:
                l_r_stack.append(curr_node.left)

            if curr_node.right:
                l_r_stack.append(curr_node.right)

if __name__ == '__main__':

    root = make_tree()

    print(spiral_traversal(root, 4))
