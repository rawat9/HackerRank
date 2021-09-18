def inOrder(root):
    if root:
        inOrder(root.left)
        print(str(root.info), end=" ")
        inOrder(root.right)