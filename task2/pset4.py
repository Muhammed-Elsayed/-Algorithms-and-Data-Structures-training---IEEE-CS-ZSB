list1 = []
colors = ["C", "M", "Y"]
x, y = input().split()
x = int(x)
y = int(y)
bolean = True
for i in range(x):
    list2 = list(map(str, input().split()))
    for k in list2:
        list1.append(k)

for letter in list1:
    if letter in colors:
        bolean = False
        print("#Color")
        break

if bolean == True:
    print('#Black&White')

