input1 = input()
list1 = list(map(int, input().split()))

counter = 0
small = big = list1[0]

for index in range(1, len(list1)):
    if list1[index] > big:
        big = list1[index]
        counter += 1

    elif list1[index] < small:
        small = list1[index]
        counter += 1

print(counter)
