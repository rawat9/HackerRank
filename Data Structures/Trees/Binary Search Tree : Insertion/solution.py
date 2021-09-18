def insert(self, val):
    node = Node(val)

    if self.root == None:
        self.root = node
    else:
        current = self.root
        while True:
            if val < current.info:
                if not current.left:
                    current.left = node
                    return self
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    return self
                current = current.right
