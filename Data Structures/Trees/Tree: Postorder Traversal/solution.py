def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(str(root.info), end=" ")
