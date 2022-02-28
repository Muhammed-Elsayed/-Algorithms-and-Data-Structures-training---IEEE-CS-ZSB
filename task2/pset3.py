cards_number = input()
list1 = list(map(int, input().split()))
sereja = 0
dima = 0
the_number = 0

def the_large(list1):
    last_index = len(list1) - 1
    if list1[0] > list1[last_index]:
        the_number = list1[0]
    else:
        the_number = list1[last_index]
    list1.remove(the_number)

    return the_number

while len(list1) != 0:

    sereja += the_large(list1)
    try:
      dima += the_large(list1)
    except:
        pass
print(sereja, dima)

