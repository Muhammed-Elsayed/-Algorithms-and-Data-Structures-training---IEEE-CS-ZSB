myinput = int(input())

w = myinput
summands = []

if myinput == 1:
    print(1)
    print(1)
    quit()

for index in range(1, myinput):
    if w > 2 * index:
       summands.append(index)
       w -= index

    else:
        summands.append(w)
        break


print(len(summands))

print(" ".join([str(index) for index in summands]))
