from node import make_tree

# determine shortest path
# determine closer nodes
# why need bellman_ford or dijkstra?
# bfs assumes all weights are same this is not the case in real world

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
