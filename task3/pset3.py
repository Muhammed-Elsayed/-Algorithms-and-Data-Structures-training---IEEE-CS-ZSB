n = int(input())
letter = input()
anton = 0
danik = 0
for index in letter:
    if index == "A":
        anton += 1
    elif index == "D":
        danik += 1

if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
elif danik == anton:
    print("Friendship")
