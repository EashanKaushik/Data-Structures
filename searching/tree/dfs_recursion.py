from node import make_tree

# dfs is good answering questions like does path exist?
# less memory than bfs
# might get slower than bfs

def inorder_traversal(root, value):

    if root:

        inorder_traversal(root.left, value)

        if(root.data == value):
            print(True)

        inorder_traversal(root.right, value)

def preorder_traversal(root, value):

    if root:

        if(root.data == value):
            print(True)

        preorder_traversal(root.left, value)

        preorder_traversal(root.right, value)

def postorder_traversal(root, value):

    if root:

        postorder_traversal(root.left, value)

        postorder_traversal(root.right, value)

        if(root.data == value):
            print(True)

if __name__ == '__main__':

    root = make_tree()

    inorder_traversal(root, 5)

    preorder_traversal(root, 5)

    postorder_traversal(root, 5)
