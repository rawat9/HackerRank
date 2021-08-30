def staircase(n):
    number_of_chars = ""
    for i in range(0, n):
        spaces = ""
        for _ in range(n - i-1):
            spaces += " "
        number_of_chars += "#"
        staircase = spaces + number_of_chars
        print(staircase)
