import string

def print_rangoli(size):
    letters = string.ascii_lowercase
    
    lst = []
    for i in range(size):
        s = "-".join(letters[i:size])
        lst.append((s[::-1] + s[1:]).center(4*size - 3, "-"))
    print('\n'.join(lst[:0:-1]+lst))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)