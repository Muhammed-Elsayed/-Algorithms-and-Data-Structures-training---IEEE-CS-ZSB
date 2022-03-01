# with run time error

x, difficulty = input().split()
list1 = list(map(int, input().split()))
counter = 0

for number in list1:
    if number <= difficulty:
        counter += 1
    else:
        break

if counter != len(list1):
    list1.reverse()
    for number in list1:
        if number <= difficulty:
            counter += 1
        else:
            break

print(counter)
