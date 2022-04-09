n = int(input())
nums = list(map(int, input().split()))
print(all(any(str(num) == str(num)[::-1] for num in nums)))
