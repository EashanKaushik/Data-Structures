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

if __name__ == '__main__':

    root = make_tree()

    print(diagonal_traversal(root, 4))
