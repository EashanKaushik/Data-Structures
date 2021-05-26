from node import make_tree

def vertical(root, value):
    queue = list()
    vertical_node_value = {}

    queue.append(root)
    queue.append(0)

    while len(queue) > 0:
        curr_node = queue.pop(0)
        curr_value = queue.pop(0)

        if curr_value in vertical_node_value:
            vertical_node_value[curr_value].append(curr_node.data)
        else:
            vertical_node_value[curr_value] = [curr_node.data]

        if curr_node.left:
            queue.append(curr_node.left)
            queue.append(curr_value - 1)

        if curr_node.right:
            queue.append(curr_node.right)
            queue.append(curr_value + 1)


    print(vertical_node_value)
    for value in sorted(vertical_node_value):
        for node in vertical_node_value[value]:
            if node == value:
                return True

if __name__ == '__main__':

    root = make_tree()

    print(vertical(root, 5))
