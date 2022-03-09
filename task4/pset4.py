n, m, k = map(float, input().split())
n, m, k = round(n), round(m), round(k * 100)
dic1 = {}
for i in range(n):
    key1, value1 = input().split()
    value1 = int(value1) * k / 100
    if value1 >= 100:
        dic1[key1] = value1

for j in range(m):
    key2 = input()
    if key2 not in dic1.keys():
      dic1[key2] = 0

print(len(dic1))
for x in sorted(dic1):
    print(x, int(dic1[x]))
