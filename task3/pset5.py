input1 = int(input())
word = input()
counter = 0
for index in range(1, len(word)):
    if word[index] == word[index - 1]:
        counter += 1

print(counter)
