n1 = int(input())
search_in_lst = list(map(int, input().split()))   # what I search in
n2 = int(input())
search_for_lst = list(map(int, input().split()))   # what I search for
output_lst = []   # output

def binary_search(search_in_lst, key):   # the key I got from (search for lst)
    left = 0
    right = len(search_in_lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if (mid == 0 or search_in_lst[mid - 1] < key) and search_in_lst[mid] == key:
            return mid

        if key > search_in_lst[mid]:
            left = mid + 1


        else:
            right = mid - 1

    return -1




for key in search_for_lst:

    x = binary_search(search_in_lst, key)
    output_lst.append(x)


print(" ".join([str(i) for i in output_lst]))




