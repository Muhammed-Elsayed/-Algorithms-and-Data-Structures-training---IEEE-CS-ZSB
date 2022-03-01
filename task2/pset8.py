
# a code that runs 
difficulty = list(map(int, input().split()))[1]
list1 = list(map(int, input().split()))
counter = 0
the_left = 0
the_right = len(list1) - 1

while the_left - the_right != 1:
    if list1[the_left] <= difficulty:
        counter += 1
        the_left += 1
    elif list1[the_right] <= difficulty:
        counter += 1
        the_right -= 1
    else:
        break
print(counter)


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

