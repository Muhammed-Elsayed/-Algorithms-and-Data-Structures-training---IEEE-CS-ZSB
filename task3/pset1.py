n = int(input())
list1 = []
value = "NO"
for index in range(n):
   input1 = input()
   list1.append(input1)

for index in range(len(list1)):
    if "OO" in list1[index]:
        value = "YES"
        list1[index] = list1[index].replace("OO", "++", 1)
        break

print(value)
if value == "YES":
    for row in list1:
        print(row)



