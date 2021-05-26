from node import make_tree

def bfs(root, value):

    queue = list()
    queue.append(root)

    while len(queue) > 0:
        curr_node = queue.pop(0)

        if curr_node.data == value:
            return True

        if curr_node.left:
            queue.append(curr_node.left)

        if curr_node.right:
            queue.append(curr_node.right)

if __name__ == '__main__':

    root = make_tree()

    print(bfs(root, 5))
