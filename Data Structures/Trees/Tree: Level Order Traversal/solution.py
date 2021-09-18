def levelOrder(root):
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        print(str(node.info), end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)