list1 = []
for index in range(5):
    input1 = list(map(int, input().split()))
    list1.append(input1)
result = 0
for i in range(5):
    for j in range(5):
        if list1[i][j] == 1:
            result += abs(i - 2)
            result += abs(j - 2)
            break

print(result)