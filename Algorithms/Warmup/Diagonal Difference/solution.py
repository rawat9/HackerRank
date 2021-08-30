def diagonalDifference(arr):
    for i in range(len(arr)-1):
        for j in range(1, len(arr)):
            print(arr[i][j], arr[j])
            i += 1     
            j += 1

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    # print(result)

# 1 2 3
# 4 5 6
# 7 8 9
