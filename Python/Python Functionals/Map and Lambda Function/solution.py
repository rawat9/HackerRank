cube = lambda x: pow(x,3) # complete the lambda function 

def fibonacci(n):
    l = [0,1]
    for i in range(2, n):
        temp = l[-1] + l[-2]
        l.append(temp)
    return l[0:n]
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))