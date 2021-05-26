from node import make_tree

def left_view(root, value):
    queue = list()

    queue.append(root)
    size = len(queue)

    while len(queue) > 0:

        curr_node = queue.pop(0)
        size -= 1

        if curr_node.right:
            queue.append(curr_node.right)

        if curr_node.left:
            queue.append(curr_node.left)

        if size == 0:
            if curr_node.data == value:
                return True
            size = len(queue)

def right_view(root, value):

    queue = list()

    queue.append(root)
    size = len(queue)

    while len(queue) > 0:

        curr_node = queue.pop(0)
        size-= 1

        if curr_node.left:
            queue.append(curr_node.left)

        if curr_node.right:
            queue.append(curr_node.right)

        if size == 0:
            if curr_node.data == value:
                return True
            size = len(queue)

def top_view(root, value):

    queue = list()
    vertical_node_value = dict()

    queue.append(root)
    queue.append(0)

    while len(queue) > 0:

        curr_node = queue.pop(0)
        curr_val = queue.pop(0)

        if curr_node.left:
            queue.append(curr_node.left)
            queue.append(curr_val - 1)

        if curr_node.right:
            queue.append(curr_node.right)
            queue.append(curr_val + 1)

        if curr_val not in vertical_node_value:
            if curr_node.data == value:
                return True
            vertical_node_value[curr_val] = curr_node.data

    # for node in sorted(vertical_node_value):
    #     print(vertical_node_value[node])

def buttom_view(root, value):
    queue = list()
    vertical_node_value = dict()

    queue.append(root)
    queue.append(0)

    while len(queue) > 0:

        curr_node = queue.pop(0)
        curr_val = queue.pop(0)

        if curr_node.left:
            queue.append(curr_node.left)
            queue.append(curr_val - 1)

        if curr_node.right:
            queue.append(curr_node.right)
            queue.append(curr_val + 1)

        if curr_val not in vertical_node_value:
            vertical_node_value[curr_val] = curr_node.data
        elif curr_val in vertical_node_value:

            if value == curr_node.data:
                return True

            vertical_node_value[curr_val] = curr_node.data

    # for value in sorted(vertical_node_value):
    #     print(vertical_node_value[value])

if __name__ == '__main__':

    root = make_tree()

    print(buttom_view(root, 4))
