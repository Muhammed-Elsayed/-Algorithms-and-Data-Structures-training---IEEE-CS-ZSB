# Uses python3
import sys

def get_change(m):
    num = 0
    while m != 0:
        if m >= 10:
            m -= 10
            num += 1
        elif m >= 5:
            m -= 5
            num += 1
        else:
            num += m
            break
    return num


myinput = int(input(""))
print(get_change(myinput))
