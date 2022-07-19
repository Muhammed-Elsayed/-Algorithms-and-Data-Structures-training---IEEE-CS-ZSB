n, W = list(map(int, input().split()))
lst = []
for i in range(n):
    value, weight = list(map(int, input().split()))

    if value == 0:
        continue

    lst.append((value, weight))


lst.sort(key=lambda x: x[0] / x[1], reverse=True)


# print(lst[0][1])
loot = 0
for v, w in lst:
    if W == 0:
        print("{:.4f}".format(loot))
        quit()

    amount = min(w, W)

    loot += amount * v / w

    W -= amount


print("{:.4f}".format(loot))
