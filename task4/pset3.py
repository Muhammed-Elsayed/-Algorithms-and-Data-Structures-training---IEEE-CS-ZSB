list1 = list(map(str, input().split("/")))

for i in range(0, list1.count('')):
    list1.remove('')

print("/" + "/".join(list1))
