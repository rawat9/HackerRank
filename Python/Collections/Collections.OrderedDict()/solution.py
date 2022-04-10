from collections import OrderedDict

n = int(input())

d = OrderedDict()

for _ in range(n):
    items = input()
    item_name, price = items.rsplit(" ", 1)
    d[item_name] = d.get(item_name, 0) + int(price)

for k, v in d.items():
    print(k, v)
