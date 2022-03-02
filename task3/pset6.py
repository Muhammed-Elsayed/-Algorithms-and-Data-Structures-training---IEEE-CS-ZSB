from math import ceil
n = int(input())
list1 = []
for x in range(n):
    list2 = []
    for y in range(n):
       if (x + y) % 2 == 0:
           list2.append("C")
       else:
           list2.append(".")
    list1.append(list2)
print(ceil(n ** 2 / 2))
for n in list1:
    print("".join(n))
