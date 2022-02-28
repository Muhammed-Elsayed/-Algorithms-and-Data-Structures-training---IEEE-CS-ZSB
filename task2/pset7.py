#first solution with a run time problem

input1 = input()
list1 = list(map(int, input().split()))
table_socks = []
counter = 0
for num in list1:
    if num not in table_socks:
        table_socks.append(num)

    else:
        table_socks.remove(num)

    if len(table_socks) > counter:
        counter = len(table_socks)

print(counter)
