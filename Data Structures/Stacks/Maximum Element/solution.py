class ArrayStack:
    def __init__(self):
        """Create an empty stack."""
        self._data = [0]

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO)."""
        return self._data.pop()


if __name__ == "__main__":
    S = ArrayStack()
    N = int(input())
    for t in range(N):
        args = list(map(int, input().split()))
        if (args[0]) == 1:
            S.push(max(args[1], S._data[-1]))
        elif (args[0]) == 2:
            S.pop()
        elif (args[0]) == 3:
            print(S._data[-1])
