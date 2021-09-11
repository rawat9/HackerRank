class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        self.peek()
        self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


if __name__ == "__main__":
    Q = Queue()
    N = int(input())
    for t in range(N):
        args = list(map(int, input().split()))
        if (args[0]) == 1:
            Q.enqueue(args[1])
        elif (args[0]) == 2:
            Q.dequeue()
        elif (args[0]) == 3:
            print(Q.peek())
