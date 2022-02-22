import math
number = int(input())
ln_of_number = math.log(number)

minimum = number / ln_of_number
maximum = 1.25506 * minimum

print(format(minimum, ".1f"), format(maximum, ".1f"))
