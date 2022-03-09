import sys
list1 = list(map(str, input().split("=")))
list2 = list1[0].split("+")

first = list(list2[0])
second = list(list2[1])
third = list(list1[1])
zero_two = [0, 2]

if len(first) >= len(second):
    bigger = first
else:
    bigger = second

if abs((len(first) + len(second)) - len(third)) not in zero_two:
    print("Impossible")
    sys.exit()

elif len(third) > (len(first) + len(second)):
    third.remove("|")
    bigger.append("|")

elif len(third) < (len(first) + len(second)):
    bigger.remove("|")
    third.append("|")

print("".join(first) + "+" + "".join(second) + "=" + "".join(third))
