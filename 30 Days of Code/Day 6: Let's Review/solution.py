def review():
    print("".join(s[::2]), "".join(s[1::2]))


if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        s = input()
        review()
