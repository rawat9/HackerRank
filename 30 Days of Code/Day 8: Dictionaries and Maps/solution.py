n = int(input())

inp = [input().split() for _ in range(n)]

dict1 = {key: value for key, value in inp}

while True:
    try:
        name = input()
        if name in dict1:
            print('{0}={1}'.format(name, dict1[name]))
        else:
            print('Not Found')
    except:
        break
