N, X = map(int, input().split())
subjects = []
for _ in range(X):
    marks = list(map(float, input().split()))
    subjects.append(marks)

print(*list(map(lambda x: sum(x) / X, zip(*subjects))), sep="\n")
