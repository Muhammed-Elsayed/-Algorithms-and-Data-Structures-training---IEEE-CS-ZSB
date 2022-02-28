size_of_list = input()
list1 = list(map(int, input().split()))
counter = len(set(list1))
if 0 in list1:
    counter -= 1
print(counter)
