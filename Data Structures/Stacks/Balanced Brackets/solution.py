class Stack:
    def __init__(self):
        self._items = []

    def push(self, val):
        self._items.append(val)

    def pop(self):
        return self._items.pop()

    def isEmpty(self):
        return len(self._items) == 0


def isBalanced(s):
    lefty = "({["
    righty = ")}]"
    mystack = Stack()
    for char in s:
        if char in lefty:
            mystack.push(char)
        elif char in righty:
            if mystack.isEmpty():
                return False
            if righty.index(char) != lefty.index(mystack.pop()):
                return False
    return mystack.isEmpty()


if __name__ == "__main__":

    t = int(input())

    for t_itr in range(t):
        s = input()
        if isBalanced(s):
            print("YES")
        else:
            print("NO")
