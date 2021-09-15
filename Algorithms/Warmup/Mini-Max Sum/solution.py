def miniMaxSum(arr):
    lowest = sum(arr) - max(arr)
    highest = sum(arr) - min(arr)
    print(lowest, highest)