if __name__ == '__main__':
    N = int(input())
    check = {True: "Not Weird", False: "Weird"}
    print(check[
        N % 2 == 0 and (
            N in range(2, 6) or
            N > 20)
    ])
