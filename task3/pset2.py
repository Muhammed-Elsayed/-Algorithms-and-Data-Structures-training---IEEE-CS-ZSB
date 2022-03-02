input1 = input()
row = input()
blocks = 0
list1 = []
counter = 0
for index in range(len(row)):
    if row[index - 1] != "B" or index == 0:
       if row[index] == "B":
          blocks += 1

    if row[index] == "B":
        counter += 1
        if index == len(row ) - 1:
            list1.append(str(counter))
            counter = 0

    if row[index] == "W":
        if counter != 0:
            list1.append(str(counter))
            counter = 0
print(blocks)
print(" ".join(list1))
