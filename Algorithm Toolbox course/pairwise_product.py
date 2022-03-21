import random
# my code the fast one
def fast_code(numbers):
    first = max(numbers)
    numbers.remove(first)
    second = max(numbers)
    return (first * second)

# the uploaded code the slow one
def slow_code(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


while True:
    numbers = []
    number_of_items_in_list = random.randint(2, 300)
    for item in range(0, number_of_items_in_list):
        numbers.append(random.randint(1, 1000))
    slow = slow_code(numbers)
    fast = fast_code(numbers)

    if slow == fast:
        print(numbers)
        print("cool it worked")
        print(f"slow : {slow} , fast : {fast}")
        print("________________")
    else:
        print(numbers)
        print("no , here we go again (sad face emoji * 1000000)")
        print(f"slow one: {slow} , fast one: {fast}")
        print("________________")
