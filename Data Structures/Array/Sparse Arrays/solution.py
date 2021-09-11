def matchingStrings(strings, queries):
    array = []
    for i in queries:
        array.append(strings.count(i))

    return array
