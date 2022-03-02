s = input()
t = input()
index = 0
for n in t:
    if n == s[index]:
        index += 1
print(index + 1)
