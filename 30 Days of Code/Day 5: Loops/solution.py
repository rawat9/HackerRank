if __name__ == '__main__':
    n = int(input())
    for i in range(1, 11):
        result = n*i
        print(f"{n} x {i} = {result}".format(n, i, result))