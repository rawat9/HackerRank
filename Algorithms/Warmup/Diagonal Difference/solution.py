def diagonalDifference(arr):
    lr_sum = rl_sum = 0
    j = len(arr) - 1
    for i in range(len(arr)):
        lr_sum += arr[i][i]
        rl_sum += arr[i][j]
        j -= 1

    return abs(lr_sum - rl_sum)