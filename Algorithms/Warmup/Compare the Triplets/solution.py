def compareTriplets(a, b):
    alice = 0
    bob = 0

    for i, j in zip(a, b):
        if i > j:
            alice += 1
        elif i < j:
            bob += 1

    return alice, bob
