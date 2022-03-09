n, p, k = map(int, input().split())
list1 = []

if p - k > 1:
    list1.append("<<")
for index in range(max((p-k), 1), min((p+k), n)+1):
      if index == p:
          list1.append("(" + str(p) + ")")
      else:
          list1.append(str(index))

if p+k < n:
    list1.append(">>")

print(" ".join(list1))
