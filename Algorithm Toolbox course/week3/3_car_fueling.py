d = int(input())  # total path
m = int(input())  # max on full tank
n = int(input())  # num of stops

stops = input().split() # list of stops
stops.append(d)


location = 0  # initialize current location
counter = 0

cons_m = m  # save the value of m

if m + location >= d:
    print(0)
    quit()


for index in range(n + 1):
    if int(stops[index]) - location > m:
        m = cons_m
        counter += 1

    # the infinity case

    if len(stops) == 0 or int(stops[index]) - location > m:
        print(-1)
        quit()


    #  the normal case
    if int(stops[index]) - location <= m:
        m -= int(stops[index]) - location
        location = int(stops[index])




print(counter)

